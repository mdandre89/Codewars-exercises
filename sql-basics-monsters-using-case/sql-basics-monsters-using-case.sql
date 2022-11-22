SELECT *,
      CASE 
          WHEN heads > arms THEN 'BEAST' 
          WHEN tails > legs THEN 'BEAST' 
          ELSE 'WEIRDO' 
      END as species
      FROM (SELECT * FROM top_half JOIN bottom_half ON top_half.id = bottom_half.id) AS h
      ORDER BY species;