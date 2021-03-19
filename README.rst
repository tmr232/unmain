unmain
======

The end to ``if __name__ == "__main__":``!


Are you tired of writing ``if __name__ == "__main__": main()`` at the end of every script?

Ever wished for a cleaner, better, simpler wait to call ``main()``?

Do you enjoy abusing the import system?

Well, today's your lucky day!


Just ``import unmain`` and we'll do the dirty work for you!

.. code-block:: python

   import unmain

   def main():
       print("Hello, unmain!")

Wow!

Installation & Usage
--------------------

Installing and using unmain is easy!

1. Install
    .. code-block:: bash

      pip install unmain

2. Import
    .. code-block:: python

         import unmain

That's it!
Unmain will find your ``main()`` function and call it for you.


Practical Considerations
------------------------

Unmain abuses the import system to re-import your main module, then running ``main()`` from it.
To avoid running global code twice - pleace ``import unmain`` at the top of your script file.
Any code above the import location will be executed twice.

Additionally, the *entire* module will execute before ``main()`` is run.
You can place your ``main()`` function anywhere in your script file.

