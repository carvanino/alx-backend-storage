-- lists all bands with Glam rock as their main style, 
-- ranked by their longevity
-- COALESCE() && IFNULL() will return use the default value 2020 to coompute
-- if split is NULL
SELECT band_name, (COALESCE(split, 2020) - formed) AS lifespan FROM metal_bands 
WHERE style LIKE '%Glam rock%' 
ORDER BY lifespan DESC;
