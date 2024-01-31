
# Question 2
Description

In the city of Toyland, there are N houses. Noddy is looking for a piece of land in the city to build his house. All the houses in the city lie in a straight line and all of them are given a house number and position of the house from the entry point of the city. Noddy wants to find the house numbers between which he can build the largest house. Write an algorithm to help Noddy to find the house numbers between which he can build his house.

Hint: No two houses will have the same position in case of multiple such answers, print the one with the least distance from the reference point.

Input Format:
The first line of the input consists of an integer num, representing the number of houses (N). The next N lines consist of two space-separated integers - house Num and pos, representing the house number and the position of the houses.
Constrairs
1.2 < num < 10^6
2. 1 < house Num < num
3. 0 < pos < 10^6

Output Format: 
Print two space-separated integers representing the house numbers in ascending order between which the largest plot is available.

Sample Input:
5
37
19
20
515
430

Sample Output:
45