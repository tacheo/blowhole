blowhole
========

.. image:: https://git.questioneer.dev/os/blowhole/badges/master/pipeline.svg
   :target: https://git.questioneer.dev/os/blowhole/pipelines

.. image:: https://git.questioneer.dev/os/blowhole/badges/master/coverage.svg
   :target: https://git.questioneer.dev/os/blowhole/pipelines

.. image:: https://img.shields.io/github/license/questioneer-ltd/blowhole.svg
   :target: https://github.com/questioneer-ltd/blowhole

.. image:: https://img.shields.io/pypi/v/blowhole.svg?color=blue
   :target: https://pypi.org/project/blowhole/

.. image:: https://img.shields.io/pypi/format/blowhole.svg?color=blue
   :target: https://pypi.org/project/blowhole/#files

.. image:: https://img.shields.io/badge/sanity-no-%233dcaad.svg
   :target: https://questioneer.co.uk/

blowhole is a tool for creating, managing, and using docker-based development (or other) environments.


Introduction
------------

Developing software often requires working with different toolchains and different development environments. Docker makes it trivial to jump into a different environment by simply launching a container, but outside of making individual Dockerfiles for each one, there's no easy way to assemble and manage these containers.

blowhole is a tool which aims to solve this problem by allowing you to easily define docker environments and share components between them, making the process of creating and jumping between environments trivial.


Features
--------

For the initial release (soon), blowhole will include the following features:

* Define environments using simple YAML syntax.
* Define modules that can be shared across different environments.
* Build and run environments using the blowhole CLI, including mounting directories and sharing ports / sockets.

A few more features are on the immediate roadmap:

* Dependency resolution between modules.
* Module configurability.

And some more features for the longer term:

* blowhole based project management (including volumes).
* Support for using a remote docker daemon over an SSH connection.

As blowhole is an open source project, we also welcome additional features and suggestions from contributors.


Advantages
----------

There are a few nice advantages to docker-based development, and in particular to blowhole.

* Known configurations - if everyone on your team is developing in the same environment, you can easily troubleshoot problems.
* Isolation - if you manage to accidentally nuke your system, doing it in a docker container is much healthier than on your physical host.
* Distro independence - run whatever distro you like, all your development environments will still work.
* Distro hopping - does your Java environment only work on Arch, while you C environment only works on Debian? Not a problem, each environment can live in a separate distro.
* Physical machine independence - want to develop on an ultralight laptop and connect to a remote development server? Sure. Want to develop locally and have zero reliance on network connectivity? Sure, you can do that too.


Development
-----------

blowhole is currently in very early development, but we're hoping to have an MVP ready for release in the near future.

Once the MVP is complete we plan to continue active development until at least all of the features described above have been addressed.


Installation
------------

As blowhole is currently in very early development, the recommended way to install is using poetry, in a virtual envrionment.

The initial release will be available on pypi and installable via pip, and we also intend to make distribution packages available for some Linux distros.
