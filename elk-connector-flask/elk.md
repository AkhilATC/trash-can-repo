## Elastic search : reference for the mapping types



| **Type**                | **ES-Type** | **Description**                                                                          |
|-------------------------|-------------|------------------------------------------------------------------------------------------|
| String , VarChar        | keyword     | This is a text field that is not tokenizable: CODE001                                    |
| String , VarChar , Text | text        | This is a text field to be tokenizated: a nice text                                      |
| Integer                 | integer     | This is an Integer (32-bit): 1,2,3, or 4                                                 |
| long                    | long        | This is a long value (64-bit)                                                            |
| float                   | float       | This is a floating-point number (32-bit): 1.2, or 4.5                                    |
| double                  | double      | This is a floating point number (64 bit)                                                 |
| boolean                 | boolean     | is a Boolean value: true or false                                                        |
| date / datetime         | date        | This is a date or datetime value: 2013-12-25 , date 2013-12-25T22:21:20                  |
| bytes / binary          | binary      | This includes some bytes that are used for binary data, such as file or stream of bytes. |



