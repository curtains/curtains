#-*-coding: utf-8-*-
"""cobject Class"""

# FIXME Event system needs review:
#
#    practicality
#    speed
#

# Notes for hackers:
#
# Pay attention to the conceptual difference between an event handler and an
# attached routine:
#
#    An attached routine is any python callable that is called whenever a
#    particular event is fired.
#
#    An event handler is a collection of objects that relate to a routine:
#
#        The routine itself
#        What arguments are preferred the routine
#        What value the routine returns when it wants to cancel an event.

import inspect
import collections

class cobject(object):
    """Base class for all objects in the curtains toolkit."""


    def __init__(self):
        """Initialize services that curtains objects require."""
        #these are for events
        self.__handlers = {}

    # events
    def attach(self, event, routine, mappings=None, cancelkey=True):
        """Attach a routine to an arbitrary event."""
        if not inspect.isroutine(routine):
            raise TypeError("'routine' must be a callable type.")

        else:
            if event not in self.__handlers.keys():
                self.__handlers[event] = []

            tup = (routine, mappings, cancelkey)
            self.__handlers[event].append(tup)

    def detach(self, event, routine):
        """Detach a routine from a specific event."""
        if event in self.__handlers.keys():
            for event_handler in self.__handlers[event]:
                attached_routine = event_handler[0]
                if attached_routine == routine:
                    self.__handlers[event].remove(event_handler)
                    break

    def fire(self, event, **kwargs):
        """Fire an arbitrary event. Return True if event cancellation was
           requested."""
        # There is no routine attached to the event, return to the caller.
        if event not in self.__handlers.keys():
            return False

        # Loop though the attached event handlers
        for event_handler in self.__handlers[event]:
            routine, mappings, cancelkey = event_handler

            # Examine the value for 'mappings' and determine how to call
            # the routine
            if isinstance(mappings, collections.Sequence):
                # If 'mappings' is a sequence, call the routine with
                # each item in the sequence as an argument.
                args = []
                for item in mappings:
                    args.append(self._get_argument_(item, kwargs))

                res = routine(*args)

            elif isinstance(mappings, collections.Mapping):
                # If 'mappings' is a mapping (dictionary), call the routine
                # with keyword arguments.
                args = {}
                for key in mappings.keys():
                    args[key] = self._get_argument_(mappings[key], kwargs)

                res = routine(**args)

            else: #default case.
                # Otherwise, call the routine with all arguments
                # arranged in ascii-alphabetical order. Seems expensive.
                keywords = sorted(kwargs.keys())
                res = routine(*[kwargs[keyw] for keyw in keywords])

            if res == cancelkey:
                return True

        return False

    def _get_argument_(self, item, kwargs):
        if isinstance(item, str):
            if item in kwargs.keys():
                # If the item is a string and is the keyword of an
                # argument, call the routine with that argument.
                return kwargs[item]

            elif item.startswith("\\") and item[1:] in kwargs.keys():
                # If the item starts with a backslash and would
                # be the keyword of an argument without it, remove
                # the backslash and call the routine with the string.
                return item[1:]

            else:
                return item

        else:
            # Otherwise call the routine with the item as is
            return item

# different namespace for these?
size = collections.namedtuple('Size', 'width height')
position = collections.namedtuple('Point', 'x y')
rect = collections.namedtuple('Rectangle', 'left top right bottom')
