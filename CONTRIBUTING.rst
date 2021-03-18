Contributing Guide
==================

Contributions are welcome and greatly appreciated!


.. _contributing-workflow-label:

Workflow
--------

A bug-fix or enhancement is delivered using a pull request. A good pull request
should cover one bug-fix or enhancement feature. This strategy ensures the
change set is easier to review and less likely to need major re-work or even be
rejected.

The workflow that developers typically use to fix a bug or add enhancements
is as follows.

* Fork the ``FragmentSoup`` repo into your account.

* Obtain the source by cloning it onto your development machine.

  .. code-block:: console

      $ git clone git@github.com:your_name_here/FragmentSoup.git
      $ cd fragmentsoup

* Create a branch for local development:

  .. code-block:: console

      $ git checkout -b name-of-your-bugfix-or-feature

  Now you can make your changes locally.

* Familiarize yourself with the developer convenience rules in the Makefile.

  .. code-block:: console

      $ make help

* Create and activate a Python virtual environment for local development. This
  rule also specifies a project specific prompt label to use once the virtual
  environment is activated.

  .. code-block:: console

      $ make venv
      $ source venv/bin/activate
      (fragmentsoup) $

  The 'venv' directory is is created under the project root directory and is
  also listed in the '.gitignore' file so that its contents never accidentally
  get added to a git change set.

  .. note::

      (fragmentsoup) is used to indicate when the commands
      should be run within the virtual environment containing the development
      dependencies.

* Develop fix or enhancement:

  * Make a fix or enhancement (e.g. modify a class, method, function, module,
    etc).

  * Update an existing unit test or create a new unit test module to verify
    the change works as expected.

  * The change should be style compliant. Perform style check.

    .. code-block:: console

        (fragmentsoup) $ make check-style

    Run 'make style' to automatically apply style fixes if needed. See the
    :ref:`style-compliance-label` section for more information.


* Commit and push changes to your fork.

  .. code-block:: console

      $ git add .
      $ git commit -m "A detailed description of the changes."
      $ git push origin name-of-your-bugfix-or-feature

  A pull request should preferably only have one commit upon the current
  master HEAD, (via rebases and squash).

* Submit a pull request through Github.
