-- ===========================================
-- NICES Lightning Monitoring Database Schema
-- ===========================================

-- Enable PostGIS (required for spatial operations)
CREATE EXTENSION IF NOT EXISTS postgis;

-- ===========================================
-- 1. CREATE TABLES
-- ===========================================

-- India states dimension table
CREATE TABLE IF NOT EXISTS india_states (
    gid SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    geom GEOMETRY(MULTIPOLYGON, 4326) NOT NULL
);

-- Create spatial index on states
CREATE INDEX IF NOT EXISTS idx_states_geom ON india_states USING GIST(geom);

-- Lightning strikes fact table
CREATE TABLE IF NOT EXISTS lightning_strikes (
    id SERIAL PRIMARY KEY,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    intensity FLOAT NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL,
    geom GEOMETRY(POINT, 4326),
    state_id INTEGER REFERENCES india_states(gid),
    batch_date DATE DEFAULT CURRENT_DATE
);

-- ===========================================
-- 2. CREATE INDEXES
-- ===========================================

-- B-tree index for time-range queries
CREATE INDEX IF NOT EXISTS idx_lightning_timestamp ON lightning_strikes(timestamp);

-- B-tree index for state joins
CREATE INDEX IF NOT EXISTS idx_lightning_state_id ON lightning_strikes(state_id);

-- GiST spatial index for geometry operations
CREATE INDEX IF NOT EXISTS idx_lightning_geom ON lightning_strikes USING GIST(geom);

-- ===========================================
-- 3. CREATE VIEWS
-- ===========================================

-- lightning_master: Enriched fact view with state names and intensity levels
CREATE OR REPLACE VIEW lightning_master AS
SELECT 
    ls.id,
    ls.latitude,
    ls.longitude,
    ls.intensity,
    ls.timestamp,
    ls.geom,
    COALESCE(s.name, 'Ocean') AS state_name,
    CASE 
        WHEN ls.intensity >= 200 THEN 'High'
        WHEN ls.intensity >= 100 THEN 'Medium'
        ELSE 'Low'
    END AS intensity_level
FROM lightning_strikes ls
LEFT JOIN india_states s ON ls.state_id = s.gid;

-- lightning_daily_summary: Aggregated daily statistics by state
CREATE OR REPLACE VIEW lightning_daily_summary AS
SELECT 
    DATE(timestamp) AS date,
    state_name,
    COUNT(*) AS daily_strikes,
    ROUND(AVG(intensity)::NUMERIC, 2) AS avg_intensity,
    MAX(intensity) AS max_intensity
FROM lightning_master
GROUP BY DATE(timestamp), state_name;

-- ===========================================
-- 4. ADD COMMENTS (Optional)
-- ===========================================

COMMENT ON TABLE lightning_strikes IS 'Raw lightning strike data from monitoring sensors';
COMMENT ON COLUMN lightning_strikes.intensity IS 'Lightning intensity in kilovolts';
COMMENT ON VIEW lightning_master IS 'Enriched lightning data with state names and intensity levels';
COMMENT ON VIEW lightning_daily_summary IS 'Daily aggregated lightning statistics by state';
