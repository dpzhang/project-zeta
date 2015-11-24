import numpy as np
from .. import affine
import os
from numpy.testing import assert_array_equal

basepath = os.path.abspath(os.path.dirname(__file__))

realpath = os.path.join(basepath, "..", "..", "..", "data", "ds105")
realpath = os.path.join(realpath, "sub001", "model", "model001")
realpath = os.path.join(realpath, "task001_run001.feat", "filtered_func_data_mni.nii.gz")
dummypath = os.path.join(basepath, "testsub001run001.nii.gz")

# The two tests below are used only when the data is in the
# appropriate place. It will be commented out so that the 
# Travis CI build passes. For Travis CI purposes, the last 
# two tests run with some dummy tests on a small subset of the
# data.

# def test_voxels_to_mm_real():
# 	voxellist = [[100, 150, 200],
# 				 [130, 145, 176],
# 				 [95, 99, 23]]
# 	x = affine.voxels_to_mm(realpath, voxellist)
# 	expected = [np.array([-110, 174, 328]),
# 				np.array([-170, 164, 280]),
# 				np.array([-100, 72, -26])]
# 	assert_array_equal(expected, x)

# def test_mm_to_voxels_real():
# 	mmlist = [np.array([-110, 174, 328]),
# 				np.array([-170, 164, 280]),
# 				np.array([-100, 72, -26])]
# 	x = affine.mm_to_voxels(realpath, mmlist)
# 	expected = [np.array([100, 150, 200]),
# 				np.array([130, 145, 176]),
# 				np.array([95, 99, 23])]
# 	assert_array_equal(expected, x)

def test_voxels_to_mm_dummy():
	voxellist = [[1, 2, 3],
				 [4, 5, 6],
				 [7, 8, 9]]
	x = affine.voxels_to_mm(dummypath, voxellist)
	expected = [np.array([1, 2, 3]),
				np.array([4, 5, 6]),
				np.array([7, 8, 9])]
	assert_array_equal(expected, x)


def test_mm_to_voxels_dummy():
	mmlist = [np.array([1, 2, 3]),
			  np.array([4, 5, 6]),
			  np.array([7, 8, 9])]
	x = affine.mm_to_voxels(dummypath, mmlist)
	expected = [np.array([1, 2, 3]),
				np.array([4, 5, 6]),
				np.array([7, 8, 9])]
	assert_array_equal(expected, x)