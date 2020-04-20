#!/usr/bin/python

# Geoffroy Blondel
# Certificat Data Science 2018



#Mapper
#Wordcount, MTD remove stop words
import sys


stopw = "a,\
about,\
above,\
across,\
after,\
afterwards,\
again,\
against,\
all,\
almost,\
alone,\
along,\
already,\
also,\
although,\
always,\
am,\
among,\
amongst,\
amoungst,\
amount,\
an,\
and,\
another,\
any,\
anyhow,\
anyone,\
anything,\
anyway,\
anywhere,\
are,\
around,\
as,\
at,\
back,\
be,\
became,\
because,\
become,\
becomes,\
becoming,\
been,\
before,\
beforehand,\
behind,\
being,\
below,\
beside,\
besides,\
between,\
beyond,\
bill,\
both,\
bottom,\
but,\
by,\
call,\
can,\
cannot,\
cant,\
co,\
computer,\
con,\
could,\
couldnt,\
cry,\
de,\
describe,\
detail,\
do,\
done,\
down,\
due,\
during,\
each,\
eg,\
eight,\
either,\
eleven,\
else,\
elsewhere,\
empty,\
enough,\
etc,\
even,\
ever,\
every,\
everyone,\
everything,\
everywhere,\
except,\
few,\
fifteen,\
fify,\
fill,\
find,\
fire,\
first,\
five,\
for,\
former,\
formerly,\
forty,\
found,\
four,\
from,\
front,\
full,\
further,\
get,\
give,\
go,\
had,\
has,\
hasnt,\
have,\
he,\
hence,\
her,\
here,\
hereafter,\
hereby,\
herein,\
hereupon,\
hers,\
herse,\
him,\
himse,\
his,\
how,\
however,\
hundred,\
i,\
ie,\
if,\
in,\
inc,\
indeed,\
interest,\
into,\
is,\
it,\
its,\
itse,\
keep,\
last,\
latter,\
latterly,\
least,\
less,\
ltd,\
made,\
many,\
may,\
me,\
meanwhile,\
might,\
mill,\
mine,\
more,\
moreover,\
most,\
mostly,\
move,\
much,\
must,\
my,\
myse,\
name,\
namely,\
neither,\
never,\
nevertheless,\
next,\
nine,\
no,\
nobody,\
none,\
noone,\
nor,\
not,\
nothing,\
now,\
nowhere,\
of,\
off,\
often,\
on,\
once,\
one,\
only,\
onto,\
or,\
other,\
others,\
otherwise,\
our,\
ours,\
ourselves,\
out,\
over,\
own,\
part,\
per,\
perhaps,\
please,\
put,\
rather,\
re,\
same,\
see,\
seem,\
seemed,\
seeming,\
seems,\
serious,\
several,\
she,\
should,\
show,\
side,\
since,\
sincere,\
six,\
sixty,\
so,\
some,\
somehow,\
someone,\
something,\
sometime,\
sometimes,\
somewhere,\
still,\
such,\
system,\
take,\
ten,\
than,\
that,\
the,\
their,\
them,\
themselves,\
then,\
thence,\
there,\
thereafter,\
thereby,\
therefore,\
therein,\
thereupon,\
these,\
they,\
thick,\
thin,\
third,\
this,\
those,\
though,\
three,\
through,\
throughout,\
thru,\
thus,\
to,\
together,\
too,\
top,\
toward,\
towards,\
twelve,\
twenty,\
two,\
un,\
under,\
until,\
up,\
upon,\
us,\
very,\
via,\
was,\
we,\
well,\
were,\
what,\
whatever,\
when,\
whence,\
whenever,\
where,\
whereafter,\
whereas,\
whereby,\
wherein,\
whereupon,\
wherever,\
whether,\
which,\
while,\
whither,\
who,\
whoever,\
whole,\
whom,\
whose,\
why,\
will,\
with,\
within,\
without,\
would,\
yet,\
you,\
your,\
yours,\
yourself,\
yourselves, <>&()-_!:;%$=+.'/?_\"	,\t,  "

# input comes from STDIN (standard input)
for line in sys.stdin:
# remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	words = line.split()
	# increase counters
	for word in words:
	#print '%s\t%s' % (word, 1)
		word = word.replace(",", "")
		word = word.replace(".", "")
		word = word.replace(";", "")
		word = word.replace(":", "")
		word = word.replace("(", "")
		word = word.replace(")", "")
		word = word.replace("?", "")
		word = word.replace("!", "")
		word = word.replace("\"", "")
		word = word.replace("\'", "")
		word = word.replace("\\", "")
		word = word.replace("/", "")
		word = word.replace("-", "")
		word = word.replace("\t", "")
		word = word.lower()
		if stopw.find(word) == -1:
			print(word + '\t' + str(1))


