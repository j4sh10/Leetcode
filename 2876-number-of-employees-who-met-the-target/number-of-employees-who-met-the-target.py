class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count_of_good_employees = 0
        for i in range(len(hours)):
            employee_hour = hours[i]
            if employee_hour >= target:
                count_of_good_employees += 1
            else:
                count_of_good_employees += 0
        return count_of_good_employees