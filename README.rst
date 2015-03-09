python-flamegraph
=================

Statistical profiler which outputs in format suitable for FlameGraph_.

INSTALL:
--------

::
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


.. _FlameGraph: http://www.brendangregg.com/flamegraphs.html
