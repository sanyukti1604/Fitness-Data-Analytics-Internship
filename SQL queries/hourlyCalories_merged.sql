use fitness_data;


------- Houlycalories_meregd.csv : removing null values ----------
   
SELECT *
FROM hourlycalories_merged
WHERE Id IS NOT NULL
  AND ActivityHour IS NOT NULL
  AND Calories IS NOT NULL;
  
SELECT * FROM hourlycalories_merged;
