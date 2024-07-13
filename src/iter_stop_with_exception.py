"""
Given that iterations are stopped raising exceptions under the hood, or so I suspect, are we underusing
this technique? maybe there are certain circumstances where it is more advantageous to let the loop loop
until it raises an exception than to check some condition every loop of the loop.
"""
