#!/usr/bin/python
# -*- coding: utf-8 -*-

#       FileName:  kalman2d.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-01-16 13:46:56
#  Last Modified:  2018-05-30 21:12:13
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

# from cv2 import cv

'''
kalman2d - 2D Kalman filter using OpenCV

Based on http://jayrambhia.wordpress.com/2012/07/26/kalman-filter/

Copyright (C) 2014 Simon D. Levy

This code is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.
This code is distributed in the hope that it will be useful,

MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this code. If not, see <http://www.gnu.org/licenses/>.
'''

import cv2
import numpy


class Kalman2D(object):

    '''
    A class for 2D Kalman filtering
    '''

    def __init__(
        self,
        processNoiseCovariance=1e-4,
        measurementNoiseCovariance=1e-1,
        errorCovariancePost=1e-1,
        ):
        '''
        For explanation of the error covariances see
        http://en.wikipedia.org/wiki/Kalman_filter
        '''

        # 状态空间：位置--2d,速度--2d

        self.kalman = cv2.KalmanFilter(4, 2, 0)

        # self.kalman_state = cv2.CreateMat(4, 1, cv.CV_32FC1)

        self.kalman_state = numpy.zeros((4, 1), numpy.float32)
        self.kalman_process_noise = numpy.zeros((4, 1), numpy.float32)

        # self.kalman_measurement = cv2.CreateMat(2, 1, cv.CV_32FC1)

        self.kalman_measurement = numpy.zeros((2, 1), numpy.float32)

        for j in range(4):
            for k in range(4):
                self.kalman.transitionMatrix[j, k] = 0
            self.kalman.transitionMatrix[j, j] = 1

        # 加入速度 x = x + vx, y = y + vy
        # 1,0,1,0,   0,1,0,1,  0,0,1,0,  0,0,0,1
        # 如果把下面两句注释掉，那么位置跟踪kalman滤波器的状态模型就是没有使用速度信息
        # self.kalman.transition_matrix[0, 2]=1
        # self.kalman.transition_matrix[1, 3]=1

        cv2.setIdentity(self.kalman.measurementMatrix)

        # 初始化带尺度的单位矩阵

        cv2.setIdentity(self.kalman.processNoiseCov,
                        cv2.RealScalar(processNoiseCovariance))
        cv2.setIdentity(self.kalman.measurementNoiseCov,
                        cv2.RealScalar(measurementNoiseCovariance))
        cv2.setIdentity(self.kalman.error_cov_post,
                        cv.RealScalar(errorCovariancePost))

        self.predicted = None
        self.esitmated = None

    def update(self, x, y):
        '''
        Updates the filter with a new X,Y measurement
        '''

        self.kalman_measurement[0, 0] = x
        self.kalman_measurement[1, 0] = y

        self.predicted = cv2.KalmanFilter.predict(self.kalman)
        self.corrected = cv2.KalmanFilter.correct(self.kalman,
                self.kalman_measurement)

    def getEstimate(self):
        '''
        Returns the current X,Y estimate.
        '''

        return (self.corrected[0, 0], self.corrected[1, 0])

    def getPrediction(self):
        '''
        Returns the current X,Y prediction.
        '''

        return (self.predicted[0, 0], self.predicted[1, 0])


