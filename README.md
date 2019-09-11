# soumitra_mazumder_version_compare_test

Problem:
The goal of this question is to write a software library that accepts 2 version string as input 
and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. 
Please provide all test cases you could think of.

Solution:
VersionCompare library is can be used to compare to version strings and returns which ever version string is greater. And if two version strings are equal then returns 'EQ'.
If the version any of the format is incorrect then it raises InvalidVersionFormatError.
VersionCompare library does not use other third party library to get the result. It uses simple arithmetic operators to decide which version string is greater.
Tast cases covered:
1> Version string input 1 is gerater than Version string input 2
2> Version string input 2 is gerater than Version string input 1
3> Version string input 1 is equal with Version string input 2


