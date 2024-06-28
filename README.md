# Residency-Stable-Matching
A sophisticated algorithm designed to match residents with their preferred hospitals

<img width="919" alt="Screenshot 2024-06-28 at 12 41 56 PM" src="https://github.com/omw2code/Residency-Stable-Matching/assets/142350438/06655dd8-ff43-405b-ab26-a1983d2a75b2">



After analyzing the benchmarks, the results meet my expectations. My program resulted in an R2 value equal to 0.9995 with respect to a second-order polynomial trend line. 
This indicates that the polynomial trend line provides a very good approximation of the relationship between the input size and the execution time of the program being O(n²). 
Analyzing my code, I believe that the while loop iterates until every hospital has been proposed to. In the worst case, this loop could iterate n times, where n is the number of residents and hospitals. Inside the while loop, there's a nested loop that iterates over each resident. In the worst case, this loop could also iterate n times. 
The nested loop structure and the operations done at each iteration result in an overall time complexity of approximately O(n²), where n is the size of the input data. This is because each resident potentially has to propose to every single hospital.
