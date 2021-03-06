+++
date = "2005-07-07T09:26:12+00:00"
title = "Join the 80-column camp!"
+++



Compared to the pre-GUI era, the typical workstation display these days is _
big_. [We're](http://www.google.com/jobs) stocking new engineers with dual
1920x1200 [
widescreens](http://accessories.us.dell.com/sna/productdetail.aspx?sku=320-4221&c=us&l=en&cs=555&category_id=2999).
That's the equivalent of six side-by-side VGA screens! In spite of this growth
over the years, my basic monitor real-estate coding rules haven't changed:
stay within 80 columns, and try to keep each function short enough to fit
vertically on a single screen.

The 80-column rule is a coding style convention that enhances readability and
helps you play nice with your teammates. I'm not sure about the origin of the
specific number 80, but it is the default width of a terminal window. A line
of a typical book also happens to average 80 characters, and a book page is
about the widest the human eye can read without getting lost in the middle.
Whatever the exact limit is, it's polite to stay within it because you don't
know the width of the window used by the person reading your code.

Resist the relentless pleas of your teammates to increase the 80-column limit.
Wider monitors enable greater productivity by allowing activities you can't do
on smaller screens, like comfortably diffing two side-by-side GUI windows of
80-column code, or debugging an application while simultaneously stepping
through its code. But you lose these new abilities if a wider monitor merely
means that your code sprawls farther and farther to the right.

The height rule is more of an engineering principle than a mere style
guideline, and as such, it's more subjective. Just as long paragraphs in a
book are tough to slog through because they contain too many ideas, [ long
functions](http://www.amazon.com/exec/obidos/tg/detail/-/0201485672/qid=1120770637/sr=8-1/ref=pd_bbs_ur_1/103-0344715-4491829?v=glance&s=books&n=507846&tag=sowbug-20)
contain too much code to understand. Splitting one long function into smaller
functions encourages documentation by forcing the programmer to give a
(possibly) meaningful name to each new function. At the same time, the
programmer will probably shorten the overall code by identifying repetitive,
copy-paste code and replacing it with calls to a single general-purpose
function.

I haven't had to adjust my function-height rule over the years, but lately
it's making me feel lonely. I'm the lone engineer on my team who hasn't
rotated his LCD to portrait position. I see no reason to do so, because it'll
only make it easier to write longer functions.

