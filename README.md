# ensemble-ops

A project initially developed as a help to data analysis related work (standard deviation of a dataset -> 2D-array) requiring enemble operations [for a friend :) ], using the `Numpy` library of Python.

Each column of the dataset represents a particular object's varying magnitude(some parameter) over a period time. All the columns of the dataset are representative of different such objects. The last two columns represent the date-time encoded as float and temperature for the object.



The processes before the ensemble operations are:
 * Dividing the dataset row-wise in groups of `a=5` rows
 * Median of each group of `a` rows.
 * Transformed matrix of all `a` rows from the original dataset
	
Ensemble operations excluding the last columns:
 * `matc_row_avg ->` transformed matrix row-wise average
 * `matc_col_avg ->` transformed matrix column-wise average
 * `matdd        ->` difference between `matc_row_avg` & `matc_col_avg` 
 * `matd_col_avg ->` `matdd` matrix column-wise average
 * `matg 	 ->` difference between `matdd` & `matd_col_avg`
 * `matg_sq 	 ->` square of `matg`
 * `matv_col_avg ->` `matg_sq` matrix column-wise average
 * `sd 		 ->` standard deviation of `matv_col_avg` 
