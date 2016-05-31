# ensemble-ops

A project initially developed as an attempt to data analysis (standard deviation of a dataset `->` 2D-array) requiring ensemble operations [for a friend], using the `Numpy` library of Python. Time & memory constraint was not an issue so the code is not optimized to its best.

## Getting started
The `new_input.txt` contains a dataset. Can be replaced with data formats other than `.txt`. `Numpy` library is a requirement to read the dataset in to a matrix.
Each column of the dataset represents a particular object's varying magnitude (some parameter) over a period time (row-wise). All the columns of the dataset are representative of different such objects. The last two columns represent the date-time encoded as float and temperature for the object.

`main.py` can be run as any other python program with the dataset present in the same path.

## Working
The processes before the ensemble operations are:
 * Dividing the dataset row-wise in groups of `a = 5` rows
 * Median of each group of `a` rows.
 * Transformed matrix of all `a` rows from the original dataset
	
Ensemble operations excluding the last two columns:
 * `matc_row_avg ->` transformed matrix row-wise average
 * `matc_col_avg ->` transformed matrix column-wise average
 * `matdd        ->` difference between `matc_row_avg` & `matc_col_avg` 
 * `matd_col_avg ->` `matdd` matrix column-wise average
 * `matg 	 ->` difference between `matdd` & `matd_col_avg`
 * `matg_sq 	 ->` square of `matg`
 * `matv_col_avg ->` `matg_sq` matrix column-wise average
 * `sd 		 ->` standard deviation of `matv_col_avg` 

## License
None. Feel free to use as is or modified at your own risk.

####### PS: If it is of any help & wish to use it for any purpose or contribute to the project, the code can be optimized or supplied with more info as required. 
