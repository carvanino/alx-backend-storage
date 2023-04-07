-- lists all bands with Glam rock as their main style, 
-- ranked by their longevity
SELECT band_name, (IFNULL(split, 2020) - formed) AS lifespan 
FROM metal_bands 
WHERE style LIKE '%Glam rock%'
ORDER BY
CASE WHEN (IFNULL(split, 2020) - formed) <> 0
	THEN lifespan
	ELSE 0
END DESC,
band_name DESC;
