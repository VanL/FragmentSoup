FragmentSoup
############

This is a thin wrapper for BeautifulSoup4 that restores the ability to work with 
HTML fragments. For example:

.. code-block:: python

    from bs4 import BeautifulSoup
    from fragmentsoup import FragmentSoup
    soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', features='html5lib')
    soup
    # <html><head></head><body><b class="boldest">Extremely bold</b></body></html>
    # Note that the fragment is wrapped to make it a valid html document

    soup = FragmentSoup('<b class="boldest">Extremely bold</b>', features='html5lib')
    soup
    # <b class="boldest">Extremely bold</b>
    # FragmentSoup keeps it as a fragment

In almost all cases, a FragmentSoup instance should work exactly the same as a
BeautifulSoup instance. The one notable exception is that calling 'wrap' on a Fragment
itself will wrap the entire Fragment and return itself:

.. code-block:: python

    from fragmentsoup import FragmentSoup
    soup = FragmentSoup('<b class="boldest">Extremely bold</b>', features='html5lib')
    soup
    # <b class="boldest">Extremely bold</b>

    soup.wrap(soup.new_tag('div') 
    # <div><b class="boldest">Extremely bold</b></div>

If you wrap a subelement, it returns a BeautifulSoup "Tag" instance. If you want to use
the returned wrapped subelement as a Fragment, you will need to wrap the returned Tag
instance to use it as a fragment:

.. code-block:: python

    from fragmentsoup import FragmentSoup
    soup = FragmentSoup('<div><b class="boldest">Extremely bold</b></div>', features='html5lib')
    subdocument = soup.b.wrap(soup.new_tag('h1'))
    subdocument
    # <h1><b class="boldest">Extremely bold</b></h1>
    type(subdocument)
    # <class 'bs4.element.Tag'>

    subdocument = FragmentSoup(subdocument)
    type(subdocument)
    # <class 'fragmentsoup.FragmentSoup'>
    

This also applies to Tags returned as a result of unwrapping a part of the document.

What if I pass in a well-formed document?
=========================================

If you pass in a full document (which is defined as starting with a <!DOCTYPE> or <html>
tag), then FragmentSoup assumes that the resulting tree is well-formed and it acts exactly
as if it were a regular BeautifulSoup instance. It will not allow you to wrap the well-formed
document with a tag - it will raise a ValueError (just as regular BeautifulSoup does).

How does it work?
=================

FragmentSoup wraps the incoming snippet in a dummy <fragmentsoup> tag that it removes (along with
all context outside the <fragmentsoup> tag before rendering. Otherwise, it defers any attribute 
accesses to an internal BeautifulSoup instance.

Bugs
====

Aside from the differences noted above, any difference in behavior from regular BeautifulSoup4
is a bug. Reports and patches welcome.

