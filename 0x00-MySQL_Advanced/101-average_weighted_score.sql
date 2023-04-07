-- Creates a stored procedure ComputeAverageWeightedScoreForUsers that 
-- computes `and store the average weighted score for all students

DELIMITER #
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users
	SET average_score = (
		SELECT SUM(weighted.score * weighted.weight) / SUM(weighted.weight)
		FROM (
			SELECT user_id, score, project_id, projects.weight 
			FROM corrections
			JOIN projects ON corrections.project_id = projects.id
			WHERE users.id = corrections.user_id
			-- AND corrections.project_id = projects.id
		) AS weighted
		GROUP BY user_id
	);
END#
