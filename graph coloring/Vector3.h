/*
 * Vector3.h
 * RVO2-3D Library
 *
 * Copyright 2008 University of North Carolina at Chapel Hill
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * Please send all bug reports to <geom@cs.unc.edu>.
 *
 * The authors may be contacted via:
 *
 * Jur van den Berg, Stephen J. Guy, Jamie Snape, Ming C. Lin, Dinesh Manocha
 * Dept. of Computer Science
 * 201 S. Columbia St.
 * Frederick P. Brooks, Jr. Computer Science Bldg.
 * Chapel Hill, N.C. 27599-3175
 * United States of America
 *
 * <http://gamma.cs.unc.edu/RVO2/>
 */

 /**
  * \file    Vector3.h
  * \brief   Contains the Vector3 class.
  */
#ifndef RVO_VECTOR3_H_
#define RVO_VECTOR3_H_

#include "API.h"

#include <cmath>
#include <cstddef>
#include <ostream>

namespace RVO {
	/**
	 * \brief  Defines a three-dimensional vector.
	 */
	class Vector3 {
	public:
		double x;
		double y;
		double z;

		/**
		 * \brief   Constructs and initializes a three-dimensional vector instance to zero.
		 */
		PF_API inline Vector3()
		{
			this->x = 0.0;
			this->y = 0.0;
			this->z = 0.0;
		}

		/**
		 * \brief   Constructs and initializes a three-dimensional vector from the specified three-dimensional vector.
		 * \param   vector  The three-dimensional vector containing the xyz-coordinates.
		 */
		PF_API inline Vector3(const Vector3& vector)
		{
			this->x = vector[0];
			this->y = vector[1];
			this->z = vector[2];
		}

		/**
		 * \brief   Constructs and initializes a three-dimensional vector from the specified three-element array.
		 * \param   val  The three-element array containing the xyz-coordinates.
		 */
		PF_API inline explicit Vector3(const double val[3])
		{
			this->x = val[0];
			this->y = val[1];
			this->z = val[2];
		}

		/**
		 * \brief   Constructs and initializes a three-dimensional vector from the specified xyz-coordinates.
		 * \param   x  The x-coordinate of the three-dimensional vector.
		 * \param   y  The y-coordinate of the three-dimensional vector.
		 * \param   z  The z-coordinate of the three-dimensional vector.
		 */
		PF_API inline Vector3(double x, double y, double z)
		{
			this->x = x;
			this->y = y;
			this->z = z;
		}

		/**
		 * \brief   Returns the specified coordinate of this three-dimensional vector.
		 * \param   i  The coordinate that should be returned (0 <= i < 3).
		 * \return  The specified coordinate of the three-dimensional vector.
		 */
		PF_API inline double operator[](size_t i) const 
		{
			if (i == 0)
				return x; 
			if (i == 1)
				return y;
			if (i == 2)
				return z;
			else
				return x;
		}

		/**
		 * \brief   Returns a reference to the specified coordinate of this three-dimensional vector.
		 * \param   i  The coordinate to which a reference should be returned (0 <= i < 3).
		 * \return  A reference to the specified coordinate of the three-dimensional vector.
		 */
		PF_API inline double& operator[](size_t i) 
		{ 
			if (i == 0)
				return x;
			if (i == 1)
				return y;
			if (i == 2)
				return z;
			return x;
		}

		/**
		 * \brief   Computes the negation of this three-dimensional vector.
		 * \return  The negation of this three-dimensional vector.
		 */
		PF_API inline Vector3 operator-() const
		{
			return Vector3(-x, -y, -z);
		}

		/**
		 * \brief   Computes the dot product of this three-dimensional vector with the specified three-dimensional vector.
		 * \param   vector  The three-dimensional vector with which the dot product should be computed.
		 * \return  The dot product of this three-dimensional vector with a specified three-dimensional vector.
		 */
		PF_API inline double operator*(const Vector3& vector) const
		{
			return x * vector[0] + y * vector[1] + z * vector[2];
		}

		/**
		 * \brief   Computes the scalar multiplication of this three-dimensional vector with the specified scalar value.
		 * \param   scalar  The scalar value with which the scalar multiplication should be computed.
		 * \return  The scalar multiplication of this three-dimensional vector with a specified scalar value.
		 */
		PF_API inline Vector3 operator*(double scalar) const
		{
			return Vector3(x * scalar, y * scalar, z * scalar);
		}

		/**
		 * \brief   Computes the scalar division of this three-dimensional vector with the specified scalar value.
		 * \param   scalar  The scalar value with which the scalar division should be computed.
		 * \return  The scalar division of this three-dimensional vector with a specified scalar value.
		 */
		PF_API inline Vector3 operator/(double scalar) const
		{
			const double invScalar = 1.0f / scalar;

			return Vector3(x * invScalar, y * invScalar, z * invScalar);
		}

		/**
		 * \brief   Computes the vector sum of this three-dimensional vector with the specified three-dimensional vector.
		 * \param   vector  The three-dimensional vector with which the vector sum should be computed.
		 * \return 	The vector sum of this three-dimensional vector with a specified three-dimensional vector.
		 */
		PF_API inline Vector3 operator+(const Vector3& vector) const
		{
			return Vector3(x + vector[0], y + vector[1], z + vector[2]);
		}

		/**
		 * \brief   Computes the vector difference of this three-dimensional vector with the specified three-dimensional vector.
		 * \param   vector  The three-dimensional vector with which the vector difference should be computed.
		 * \return  The vector difference of this three-dimensional vector with a specified three-dimensional vector.
		 */
		PF_API inline Vector3 operator-(const Vector3& vector) const
		{
			return Vector3(x - vector[0], y - vector[1], z - vector[2]);
		}

		/**
		 * \brief   Tests this three-dimensional vector for equality with the specified three-dimensional vector.
		 * \param   vector  The three-dimensional vector with which to test for equality.
		 * \return  True if the three-dimensional vectors are equal.
		 */
		PF_API inline bool operator==(const Vector3& vector) const
		{
			return x == vector[0] && y == vector[1] && z == vector[2];
		}

		/**
		 * \brief   Tests this three-dimensional vector for inequality with the specified three-dimensional vector.
		 * \param   vector  The three-dimensional vector with which to test for inequality.
		 * \return  True if the three-dimensional vectors are not equal.
		 */
		PF_API inline bool operator!=(const Vector3& vector) const
		{
			return x != vector[0] || y != vector[1] || z != vector[2];
		}

		/**
		 * \brief   Sets the value of this three-dimensional vector to the scalar multiplication of itself with the specified scalar value.
		 * \param   scalar  The scalar value with which the scalar multiplication should be computed.
		 * \return  A reference to this three-dimensional vector.
		 */
		PF_API inline Vector3& operator*=(double scalar)
		{
			x *= scalar;
			y *= scalar;
			z *= scalar;

			return *this;
		}

		/**
		 * \brief   Sets the value of this three-dimensional vector to the scalar division of itself with the specified scalar value.
		 * \param   scalar  The scalar value with which the scalar division should be computed.
		 * \return  A reference to this three-dimensional vector.
		 */
		PF_API inline Vector3& operator/=(double scalar)
		{
			const double invScalar = 1.0f / scalar;

			x *= invScalar;
			y *= invScalar;
			z *= invScalar;

			return *this;
		}

		/**
		 * \brief   Sets the value of this three-dimensional vector to the vector
		 *             sum of itself with the specified three-dimensional vector.
		 * \param   vector  The three-dimensional vector with which the vector sum should be computed.
		 * \return  A reference to this three-dimensional vector.
		 */
		PF_API inline Vector3& operator+=(const Vector3& vector)
		{
			x += vector[0];
			y += vector[1];
			z += vector[2];

			return *this;
		}

		/**
		 * \brief   Sets the value of this three-dimensional vector to the vector difference of itself with the specified three-dimensional vector.
		 * \param   vector  The three-dimensional vector with which the vector difference should be computed.
		 * \return  A reference to this three-dimensional vector.
		 */
		PF_API inline Vector3& operator-=(const Vector3& vector)
		{
			x -= vector[0];
			y -= vector[1];
			z -= vector[2];

			return *this;
		}

		PF_API inline Vector3& operator=(const Vector3& vector)
		{
			x = vector[0];
			y = vector[1];
			z = vector[2];

			return *this;
		}

		/**
		 * \relates  Vector3
		 * \brief    Computes the normalization of the specified three-dimensional vector.
		 * \return   The normalization of the three-dimensional vector.
		 */
		PF_API inline double length()
		{
			return std::sqrt(x * x + y * y + z * z);
		}

	private:

	};


	/**
	 * \relates  Vector3
	 * \brief    Computes the scalar multiplication of the specified three-dimensional vector with the specified scalar value.
	 * \param    scalar  The scalar value with which the scalar multiplication should be computed.
	 * \param    vector  The three-dimensional vector with which the scalar multiplication should be computed.
	 * \return   The scalar multiplication of the three-dimensional vector with the scalar value.
	 */
	inline Vector3 operator*(double scalar, const Vector3& vector)
	{
		return Vector3(scalar * vector[0], scalar * vector[1], scalar * vector[2]);
	}

	/**
	 * \relates  Vector3
	 * \brief    Computes the cross product of the specified three-dimensional vectors.
	 * \param    vector1  The first vector with which the cross product should be computed.
	 * \param    vector2  The second vector with which the cross product should be computed.
	 * \return   The cross product of the two specified vectors.
	 */
	inline Vector3 cross(const Vector3& vector1, const Vector3& vector2)
	{
		return Vector3(vector1[1] * vector2[2] - vector1[2] * vector2[1], vector1[2] * vector2[0] - vector1[0] * vector2[2], vector1[0] * vector2[1] - vector1[1] * vector2[0]);
	}

	/**
	 * \relates  Vector3
	 * \brief    Inserts the specified three-dimensional vector into the specified output stream.
	 * \param    os      The output stream into which the three-dimensional vector should be inserted.
	 * \param    vector  The three-dimensional vector which to insert into the output stream.
	 * \return   A reference to the output stream.
	 */
	inline std::ostream& operator<<(std::ostream& os, const Vector3& vector)
	{
		os << "(" << vector[0] << "," << vector[1] << "," << vector[2] << ")";

		return os;
	}

	/**
	 * \relates  Vector3
	 * \brief    Computes the length of a specified three-dimensional vector.
	 * \param    vector  The three-dimensional vector whose length is to be computed.
	 * \return   The length of the three-dimensional vector.
	 */
	inline double abs(const Vector3& vector)
	{
		return std::sqrt(vector * vector);
	}

	/**
	 * \relates  Vector3
	 * \brief    Computes the squared length of a specified three-dimensional vector.
	 * \param    vector  The three-dimensional vector whose squared length is to be computed.
	 * \return   The squared length of the three-dimensional vector.
	 */
	inline double absSq(const Vector3& vector)
	{
		return vector * vector;
	}

	/**
	 * \relates  Vector3
	 * \brief    Computes the normalization of the specified three-dimensional vector.
	 * \param    vector  The three-dimensional vector whose normalization is to be computed.
	 * \return   The normalization of the three-dimensional vector.
	 */
	inline Vector3 normalize(const Vector3& vector)
	{
		return vector / abs(vector);
	}

}

#endif
