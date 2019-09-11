# soumitra_mazumder_version_compare_test

<b>Problem:</b></br>
The goal of this question is to write a software library that accepts 2 version string as input 
and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. 
Please provide all test cases you could think of.

<b>Solution:</b> </br>
VersionCompare library is can be used to compare to version strings and returns which ever version string is greater. And if two version strings are equal then returns 'EQ'.
If the version any of the format is incorrect then it raises InvalidVersionFormatError.
VersionCompare library does not use other third party library to get the result. It uses simple arithmetic operators to decide which version string is greater.
<b>Usage:</b></br>
One can import the VersionCompair library and  use it as below: </br>
        <b>version_string_a = '1.2.1.1'  </br>
        version_string_b = '1.2.1.1'  </br>
        version_compare = VersionCompare()  </br>
        version_a_list, version_b_list = version_compare.get_version_string_as_list(version_string_a, version_string_b)  </br>
        return_version_string = version_compare.compare_versions_input(version_a_list, version_b_list)  </br>
        </br></b>
<b>Tast cases covered: </b></br>
1> Version string input 1 is gerater than Version string input 2 </br>
2> Version string input 2 is gerater than Version string input 1 </br>
3> Version string input 1 is equal with Version string input 2 </br>
4> Version string for example "1.3.2." or "1.3.A" is considered as invalid version  </br>


