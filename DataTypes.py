#FILE HOLDING RHINESTONE DATA TYPES

from pyparsing import Optional, Word,nums,alphanums,ZeroOrMore,alphas,oneOf,Forward,CaselessLiteral

integer = Optional('-') + Word(nums)
floating = Optional('-') + integer + '.' + integer
String = "'" + ZeroOrMore(Word(alphanums)) + "'" | '"' + ZeroOrMore(Word(alphanums)) + '"' \
         | '"' + ZeroOrMore(Word(alphanums)) + "'" | "'" + ZeroOrMore(Word(alphanums)) + '"'
sglq = "'"
dblq = '"'
char = sglq + oneOf('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0') + sglq \
| dblq + oneOf('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0') + dblq \
| sglq + oneOf('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0') + dblq \
| dblq + oneOf('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0') + sglq
Dictionary = Forward #Implement later
Possibly_a = Forward #Implement later
List = Forward #Implement later
comment = Forward #No declaration for comment data type
boolean = CaselessLiteral('t:').setParseAction(lambda t: True) | CaselessLiteral('f:').setParseAction(lambda t: False)
