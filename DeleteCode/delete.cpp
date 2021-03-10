	/* Set the preferred velocity to be a vector of unit magnitude (speed) in the direction of the goal. */
	for (size_t index = 0; index < sim.getNumAgents(); ++index) {
		Vector3 goalVector = Vector3(end_position[index].x, end_position[index].y, end_position[index].z) - sim.getAgentPosition(index);

		if (filter[index] <= (rel_time / frame_time * 1000.0 + start_frame+0.001))
		{
			if (absSq(goalVector) > 1.0f) {
				goalVector = normalize(goalVector);
			}
			sim.setAgentRadius(index, safe_dis);
			sim.setAgentPrefVelocity(index, goalVector);
		}
		else
		{
			//debug_print << "wait:" << index << endl;
			cur_position[index] = start_position[index];
			sim.setAgentPrefVelocity(index, Vector3(0, 0, 0));
			sim.setAgentRadius(index, 0.0);
			sim.setAgentPosition(index, Vector3(start_position[index].x, start_position[index].y, start_position[index].z));
		}
	}