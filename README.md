# sorting
My various projects on sorting in Python. The main part is a mix of pure-Python and processing, which is a project in progress, hoping to get some clean, efficient sorting implementations in Python and visualise them (in the classic points fashion, with added rainbows and exponential decay to demonstrate array accesses) in addition to providing command-line support. `pure` contains pure implementations - in the main directory generator versions are provided (which allow the sort to block itself while keeping state, and allow the generator to provide information about where it's working for rainbow access visualistion). They're also Python 2 as that's my processing installation, so there are some `xrange`s etc.

Here is Quicksort, for example:

![screenshot](https://github.com/elterminad0r/sorting/blob/master/quick.png)

And merge-sort:

![screenshot](https://github.com/elterminad0r/sorting/blob/master/merge.png)

Heapsort:

![screenshot](https://github.com/elterminad0r/sorting/blob/master/heap.png)

So far it also features bubble-sort and bogosort (the former is miniaturised and sped up and still takes forever to complete - the second just takes forever to complete). I'm only doing algorithms than can be implemented somewhat in place without too much trickery, as this allows the visualisation (merge-sort does make some auxiliary arrays but it still shows the accesses in the merging).

It also features an old, old directory (`school`) from when I was in year 10 and did an investigation into sorting algorithms, which devolved into comparison-less integer sorting. It's a mess. 
