use fitness_data;
-------- hourlysteps_merged : removing null values ----------
  
SELECT * 
FROM hourlysteps_merged
WHERE Id IS NOT NULL
  AND ActivityHour IS NOT NULL
  AND StepTotal  IS NOT NULL;
  
