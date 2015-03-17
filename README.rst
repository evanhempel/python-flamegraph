A simple statistical profiler which outputs in format suitable for FlameGraph_.

INSTALL:
--------

Simply run::

  pip install git+https://github.com/evanhempel/python-flamegraph.git

USAGE:
------

Run your script under the profiler::

  python -m flamegraph -o perf.log myscript.py --your-script args here

Run Brendan Gregg's FlameGraph_ tool against the output::

  flamegraph.pl --title "MyScript CPU" perf.log > perf.svg

Enjoy the output:

.. image:: docs/attic-create.png
  :alt: Attic create flame graph
  :width: 679
  :height: 781
  :align: center

**Filtering**

Sometimes you may want to exclude a method 
(for example in a server the method that waits for a new request)
or you may want to profile only a subset of your code
(a particular method and its children which are performance critical).
Since the output is stackframes each on a line by itself,
this can simply be done with a simple grep filter.

Exclude::

    grep -v waiting_method perf.log > removed_waiting.log

Include:: 

    grep function_name perf.log > filtered.log

Then run the flamegraph.pl script against the filtered file.

.. _FlameGraph: http://www.brendangregg.com/flamegraphs.html
