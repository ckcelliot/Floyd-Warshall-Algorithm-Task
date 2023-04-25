# Floyd-Warshall-Algorithm-Task

Task Requirements:
1. Write to PEP standards
2. Put under source control
3. Write unit tests for each function
4. Write performance tests
5. Check the version against the one located at the website
6. Include directory tree and code documentation (readme.md and requirements.txt)
7. Report


Report Requirements:
1. Discuss how the application was built

2. How to create the tests and the coverage of your tests

3. Try to have a hypothesis to explain the differences between the performance of the iterative version on the PDF and your own recursive version



# Directory Tree


```
C:\Users\rohba\OneDrive\Desktop\Fiv 3\
│
├── .git\
│   │
│   ├── hooks\
│   │   ├── applypatch-msg.sample
│   │   ├── commit-msg.sample
│   │   ├── fsmonitor-watchman.sample
│   │   ├── post-update.sample
│   │   ├── pre-applypatch.sample
│   │   ├── pre-commit.sample
│   │   ├── pre-merge-commit.sample
│   │   ├── pre-push.sample
│   │   ├── pre-rebase.sample
│   │   ├── pre-receive.sample
│   │   ├── prepare-commit-msg.sample
│   │   ├── push-to-checkout.sample
│   │   └── update.sample
│   │
│   ├── info\
│   │   └── exclude
│   │
│   ├── logs\
│   │   │
│   │   ├── refs\
│   │   │   │
│   │   │   └── heads\
│   │   │       └── master
│   │   │
│   │   │
│   │   └── HEAD
│   │
│   ├── objects\
│   │   │
│   │   ├── 3a\
│   │   │   └── fe6d1521723949be3dcae2b56bb43334012cb1
│   │   │
│   │   ├── 5b\
│   │   │   └── 7db92f44001a051fc86e44334e914f0153970e
│   │   │
│   │   ├── 71\
│   │   │   └── 545a98debc04e599016841f669ef4d14bc0214
│   │   │
│   │   ├── 7b\
│   │   │   └── b9d049665e8fd53399df064f3d6333063b5b6c
│   │   │
│   │   ├── 85\
│   │   │   └── e5916095619054303b6884d32117e98bbd84c6
│   │   │
│   │   ├── 95\
│   │   │   └── 15190363785a5dbe46b4ea01767b51f1babf0c
│   │   │
│   │   ├── c9\
│   │   │   └── 4831a7a0f04fe877799828010b2145db2d46db
│   │   │
│   │   ├── e1\
│   │   │   └── 3ef80bb4014ffd159ec21b08a3904f4af3fe8f
│   │   │
│   │   ├── f6\
│   │   │   └── 9bf4b8a7521bbc821aa381204a4ca528ff8977
│   │   │
│   │   ├── info\
│   │   │
│   │   └── pack\
│   │
│   │
│   ├── refs\
│   │   │
│   │   ├── heads\
│   │   │   └── master
│   │   │
│   │   └── tags\
│   │
│   │
│   ├── COMMIT_EDITMSG
│   ├── HEAD
│   ├── config
│   ├── description
│   └── index
│
├── __pycache__\
│   ├── Geek4Geek.cpython-310.pyc
│   ├── fiv.cpython-310.pyc
│   ├── fiv_rec.cpython-310.pyc
│   ├── floyd.cpython-310.pyc
│   ├── floyd_rec.cpython-310.pyc
│   └── unittest.cpython-310.pyc
│
├── venv\
│   │
│   ├── Include\
│   │
│   ├── Lib\
│   │   │
│   │   └── site-packages\
│   │       │
│   │       ├── _distutils_hack\
│   │       │   │
│   │       │   ├── __pycache__\
│   │       │   │   ├── __init__.cpython-310.pyc
│   │       │   │   └── override.cpython-310.pyc
│   │       │   │
│   │       │   ├── __init__.py
│   │       │   └── override.py
│   │       │
│   │       ├── pip\
│   │       │   │
│   │       │   ├── __pycache__\
│   │       │   │   ├── __init__.cpython-310.pyc
│   │       │   │   ├── __main__.cpython-310.pyc
│   │       │   │   └── __pip-runner__.cpython-310.pyc
│   │       │   │
│   │       │   ├── _internal\
│   │       │   │   │
│   │       │   │   ├── __pycache__\
│   │       │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   ├── build_env.cpython-310.pyc
│   │       │   │   │   ├── cache.cpython-310.pyc
│   │       │   │   │   ├── configuration.cpython-310.pyc
│   │       │   │   │   ├── exceptions.cpython-310.pyc
│   │       │   │   │   ├── main.cpython-310.pyc
│   │       │   │   │   ├── pyproject.cpython-310.pyc
│   │       │   │   │   ├── self_outdated_check.cpython-310.pyc
│   │       │   │   │   └── wheel_builder.cpython-310.pyc
│   │       │   │   │
│   │       │   │   ├── cli\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── autocompletion.cpython-310.pyc
│   │       │   │   │   │   ├── base_command.cpython-310.pyc
│   │       │   │   │   │   ├── cmdoptions.cpython-310.pyc
│   │       │   │   │   │   ├── command_context.cpython-310.pyc
│   │       │   │   │   │   ├── main.cpython-310.pyc
│   │       │   │   │   │   ├── main_parser.cpython-310.pyc
│   │       │   │   │   │   ├── parser.cpython-310.pyc
│   │       │   │   │   │   ├── progress_bars.cpython-310.pyc
│   │       │   │   │   │   ├── req_command.cpython-310.pyc
│   │       │   │   │   │   ├── spinners.cpython-310.pyc
│   │       │   │   │   │   └── status_codes.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── autocompletion.py
│   │       │   │   │   ├── base_command.py
│   │       │   │   │   ├── cmdoptions.py
│   │       │   │   │   ├── command_context.py
│   │       │   │   │   ├── main.py
│   │       │   │   │   ├── main_parser.py
│   │       │   │   │   ├── parser.py
│   │       │   │   │   ├── progress_bars.py
│   │       │   │   │   ├── req_command.py
│   │       │   │   │   ├── spinners.py
│   │       │   │   │   └── status_codes.py
│   │       │   │   │
│   │       │   │   ├── commands\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── cache.cpython-310.pyc
│   │       │   │   │   │   ├── check.cpython-310.pyc
│   │       │   │   │   │   ├── completion.cpython-310.pyc
│   │       │   │   │   │   ├── configuration.cpython-310.pyc
│   │       │   │   │   │   ├── debug.cpython-310.pyc
│   │       │   │   │   │   ├── download.cpython-310.pyc
│   │       │   │   │   │   ├── freeze.cpython-310.pyc
│   │       │   │   │   │   ├── hash.cpython-310.pyc
│   │       │   │   │   │   ├── help.cpython-310.pyc
│   │       │   │   │   │   ├── index.cpython-310.pyc
│   │       │   │   │   │   ├── inspect.cpython-310.pyc
│   │       │   │   │   │   ├── install.cpython-310.pyc
│   │       │   │   │   │   ├── list.cpython-310.pyc
│   │       │   │   │   │   ├── search.cpython-310.pyc
│   │       │   │   │   │   ├── show.cpython-310.pyc
│   │       │   │   │   │   ├── uninstall.cpython-310.pyc
│   │       │   │   │   │   └── wheel.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── cache.py
│   │       │   │   │   ├── check.py
│   │       │   │   │   ├── completion.py
│   │       │   │   │   ├── configuration.py
│   │       │   │   │   ├── debug.py
│   │       │   │   │   ├── download.py
│   │       │   │   │   ├── freeze.py
│   │       │   │   │   ├── hash.py
│   │       │   │   │   ├── help.py
│   │       │   │   │   ├── index.py
│   │       │   │   │   ├── inspect.py
│   │       │   │   │   ├── install.py
│   │       │   │   │   ├── list.py
│   │       │   │   │   ├── search.py
│   │       │   │   │   ├── show.py
│   │       │   │   │   ├── uninstall.py
│   │       │   │   │   └── wheel.py
│   │       │   │   │
│   │       │   │   ├── distributions\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── base.cpython-310.pyc
│   │       │   │   │   │   ├── installed.cpython-310.pyc
│   │       │   │   │   │   ├── sdist.cpython-310.pyc
│   │       │   │   │   │   └── wheel.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── base.py
│   │       │   │   │   ├── installed.py
│   │       │   │   │   ├── sdist.py
│   │       │   │   │   └── wheel.py
│   │       │   │   │
│   │       │   │   ├── index\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── collector.cpython-310.pyc
│   │       │   │   │   │   ├── package_finder.cpython-310.pyc
│   │       │   │   │   │   └── sources.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── collector.py
│   │       │   │   │   ├── package_finder.py
│   │       │   │   │   └── sources.py
│   │       │   │   │
│   │       │   │   ├── locations\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── _distutils.cpython-310.pyc
│   │       │   │   │   │   ├── _sysconfig.cpython-310.pyc
│   │       │   │   │   │   └── base.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _distutils.py
│   │       │   │   │   ├── _sysconfig.py
│   │       │   │   │   └── base.py
│   │       │   │   │
│   │       │   │   ├── metadata\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── _json.cpython-310.pyc
│   │       │   │   │   │   ├── base.cpython-310.pyc
│   │       │   │   │   │   └── pkg_resources.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── importlib\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   │   ├── _compat.cpython-310.pyc
│   │       │   │   │   │   │   ├── _dists.cpython-310.pyc
│   │       │   │   │   │   │   └── _envs.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── _compat.py
│   │       │   │   │   │   ├── _dists.py
│   │       │   │   │   │   └── _envs.py
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _json.py
│   │       │   │   │   ├── base.py
│   │       │   │   │   └── pkg_resources.py
│   │       │   │   │
│   │       │   │   ├── models\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── candidate.cpython-310.pyc
│   │       │   │   │   │   ├── direct_url.cpython-310.pyc
│   │       │   │   │   │   ├── format_control.cpython-310.pyc
│   │       │   │   │   │   ├── index.cpython-310.pyc
│   │       │   │   │   │   ├── installation_report.cpython-310.pyc
│   │       │   │   │   │   ├── link.cpython-310.pyc
│   │       │   │   │   │   ├── scheme.cpython-310.pyc
│   │       │   │   │   │   ├── search_scope.cpython-310.pyc
│   │       │   │   │   │   ├── selection_prefs.cpython-310.pyc
│   │       │   │   │   │   ├── target_python.cpython-310.pyc
│   │       │   │   │   │   └── wheel.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── candidate.py
│   │       │   │   │   ├── direct_url.py
│   │       │   │   │   ├── format_control.py
│   │       │   │   │   ├── index.py
│   │       │   │   │   ├── installation_report.py
│   │       │   │   │   ├── link.py
│   │       │   │   │   ├── scheme.py
│   │       │   │   │   ├── search_scope.py
│   │       │   │   │   ├── selection_prefs.py
│   │       │   │   │   ├── target_python.py
│   │       │   │   │   └── wheel.py
│   │       │   │   │
│   │       │   │   ├── network\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── auth.cpython-310.pyc
│   │       │   │   │   │   ├── cache.cpython-310.pyc
│   │       │   │   │   │   ├── download.cpython-310.pyc
│   │       │   │   │   │   ├── lazy_wheel.cpython-310.pyc
│   │       │   │   │   │   ├── session.cpython-310.pyc
│   │       │   │   │   │   ├── utils.cpython-310.pyc
│   │       │   │   │   │   └── xmlrpc.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── auth.py
│   │       │   │   │   ├── cache.py
│   │       │   │   │   ├── download.py
│   │       │   │   │   ├── lazy_wheel.py
│   │       │   │   │   ├── session.py
│   │       │   │   │   ├── utils.py
│   │       │   │   │   └── xmlrpc.py
│   │       │   │   │
│   │       │   │   ├── operations\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── check.cpython-310.pyc
│   │       │   │   │   │   ├── freeze.cpython-310.pyc
│   │       │   │   │   │   └── prepare.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── build\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   │   ├── build_tracker.cpython-310.pyc
│   │       │   │   │   │   │   ├── metadata.cpython-310.pyc
│   │       │   │   │   │   │   ├── metadata_editable.cpython-310.pyc
│   │       │   │   │   │   │   ├── metadata_legacy.cpython-310.pyc
│   │       │   │   │   │   │   ├── wheel.cpython-310.pyc
│   │       │   │   │   │   │   ├── wheel_editable.cpython-310.pyc
│   │       │   │   │   │   │   └── wheel_legacy.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── build_tracker.py
│   │       │   │   │   │   ├── metadata.py
│   │       │   │   │   │   ├── metadata_editable.py
│   │       │   │   │   │   ├── metadata_legacy.py
│   │       │   │   │   │   ├── wheel.py
│   │       │   │   │   │   ├── wheel_editable.py
│   │       │   │   │   │   └── wheel_legacy.py
│   │       │   │   │   │
│   │       │   │   │   ├── install\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   │   ├── editable_legacy.cpython-310.pyc
│   │       │   │   │   │   │   ├── legacy.cpython-310.pyc
│   │       │   │   │   │   │   └── wheel.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── editable_legacy.py
│   │       │   │   │   │   ├── legacy.py
│   │       │   │   │   │   └── wheel.py
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── check.py
│   │       │   │   │   ├── freeze.py
│   │       │   │   │   └── prepare.py
│   │       │   │   │
│   │       │   │   ├── req\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── constructors.cpython-310.pyc
│   │       │   │   │   │   ├── req_file.cpython-310.pyc
│   │       │   │   │   │   ├── req_install.cpython-310.pyc
│   │       │   │   │   │   ├── req_set.cpython-310.pyc
│   │       │   │   │   │   └── req_uninstall.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── constructors.py
│   │       │   │   │   ├── req_file.py
│   │       │   │   │   ├── req_install.py
│   │       │   │   │   ├── req_set.py
│   │       │   │   │   └── req_uninstall.py
│   │       │   │   │
│   │       │   │   ├── resolution\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   └── base.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── legacy\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   │   └── resolver.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   └── resolver.py
│   │       │   │   │   │
│   │       │   │   │   ├── resolvelib\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   │   ├── base.cpython-310.pyc
│   │       │   │   │   │   │   ├── candidates.cpython-310.pyc
│   │       │   │   │   │   │   ├── factory.cpython-310.pyc
│   │       │   │   │   │   │   ├── found_candidates.cpython-310.pyc
│   │       │   │   │   │   │   ├── provider.cpython-310.pyc
│   │       │   │   │   │   │   ├── reporter.cpython-310.pyc
│   │       │   │   │   │   │   ├── requirements.cpython-310.pyc
│   │       │   │   │   │   │   └── resolver.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── base.py
│   │       │   │   │   │   ├── candidates.py
│   │       │   │   │   │   ├── factory.py
│   │       │   │   │   │   ├── found_candidates.py
│   │       │   │   │   │   ├── provider.py
│   │       │   │   │   │   ├── reporter.py
│   │       │   │   │   │   ├── requirements.py
│   │       │   │   │   │   └── resolver.py
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   └── base.py
│   │       │   │   │
│   │       │   │   ├── utils\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── _log.cpython-310.pyc
│   │       │   │   │   │   ├── appdirs.cpython-310.pyc
│   │       │   │   │   │   ├── compat.cpython-310.pyc
│   │       │   │   │   │   ├── compatibility_tags.cpython-310.pyc
│   │       │   │   │   │   ├── datetime.cpython-310.pyc
│   │       │   │   │   │   ├── deprecation.cpython-310.pyc
│   │       │   │   │   │   ├── direct_url_helpers.cpython-310.pyc
│   │       │   │   │   │   ├── distutils_args.cpython-310.pyc
│   │       │   │   │   │   ├── egg_link.cpython-310.pyc
│   │       │   │   │   │   ├── encoding.cpython-310.pyc
│   │       │   │   │   │   ├── entrypoints.cpython-310.pyc
│   │       │   │   │   │   ├── filesystem.cpython-310.pyc
│   │       │   │   │   │   ├── filetypes.cpython-310.pyc
│   │       │   │   │   │   ├── glibc.cpython-310.pyc
│   │       │   │   │   │   ├── hashes.cpython-310.pyc
│   │       │   │   │   │   ├── inject_securetransport.cpython-310.pyc
│   │       │   │   │   │   ├── logging.cpython-310.pyc
│   │       │   │   │   │   ├── misc.cpython-310.pyc
│   │       │   │   │   │   ├── models.cpython-310.pyc
│   │       │   │   │   │   ├── packaging.cpython-310.pyc
│   │       │   │   │   │   ├── setuptools_build.cpython-310.pyc
│   │       │   │   │   │   ├── subprocess.cpython-310.pyc
│   │       │   │   │   │   ├── temp_dir.cpython-310.pyc
│   │       │   │   │   │   ├── unpacking.cpython-310.pyc
│   │       │   │   │   │   ├── urls.cpython-310.pyc
│   │       │   │   │   │   ├── virtualenv.cpython-310.pyc
│   │       │   │   │   │   └── wheel.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _log.py
│   │       │   │   │   ├── appdirs.py
│   │       │   │   │   ├── compat.py
│   │       │   │   │   ├── compatibility_tags.py
│   │       │   │   │   ├── datetime.py
│   │       │   │   │   ├── deprecation.py
│   │       │   │   │   ├── direct_url_helpers.py
│   │       │   │   │   ├── distutils_args.py
│   │       │   │   │   ├── egg_link.py
│   │       │   │   │   ├── encoding.py
│   │       │   │   │   ├── entrypoints.py
│   │       │   │   │   ├── filesystem.py
│   │       │   │   │   ├── filetypes.py
│   │       │   │   │   ├── glibc.py
│   │       │   │   │   ├── hashes.py
│   │       │   │   │   ├── inject_securetransport.py
│   │       │   │   │   ├── logging.py
│   │       │   │   │   ├── misc.py
│   │       │   │   │   ├── models.py
│   │       │   │   │   ├── packaging.py
│   │       │   │   │   ├── setuptools_build.py
│   │       │   │   │   ├── subprocess.py
│   │       │   │   │   ├── temp_dir.py
│   │       │   │   │   ├── unpacking.py
│   │       │   │   │   ├── urls.py
│   │       │   │   │   ├── virtualenv.py
│   │       │   │   │   └── wheel.py
│   │       │   │   │
│   │       │   │   ├── vcs\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── bazaar.cpython-310.pyc
│   │       │   │   │   │   ├── git.cpython-310.pyc
│   │       │   │   │   │   ├── mercurial.cpython-310.pyc
│   │       │   │   │   │   ├── subversion.cpython-310.pyc
│   │       │   │   │   │   └── versioncontrol.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── bazaar.py
│   │       │   │   │   ├── git.py
│   │       │   │   │   ├── mercurial.py
│   │       │   │   │   ├── subversion.py
│   │       │   │   │   └── versioncontrol.py
│   │       │   │   │
│   │       │   │   ├── __init__.py
│   │       │   │   ├── build_env.py
│   │       │   │   ├── cache.py
│   │       │   │   ├── configuration.py
│   │       │   │   ├── exceptions.py
│   │       │   │   ├── main.py
│   │       │   │   ├── pyproject.py
│   │       │   │   ├── self_outdated_check.py
│   │       │   │   └── wheel_builder.py
│   │       │   │
│   │       │   ├── _vendor\
│   │       │   │   │
│   │       │   │   ├── __pycache__\
│   │       │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   ├── six.cpython-310.pyc
│   │       │   │   │   └── typing_extensions.cpython-310.pyc
│   │       │   │   │
│   │       │   │   ├── cachecontrol\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── _cmd.cpython-310.pyc
│   │       │   │   │   │   ├── adapter.cpython-310.pyc
│   │       │   │   │   │   ├── cache.cpython-310.pyc
│   │       │   │   │   │   ├── compat.cpython-310.pyc
│   │       │   │   │   │   ├── controller.cpython-310.pyc
│   │       │   │   │   │   ├── filewrapper.cpython-310.pyc
│   │       │   │   │   │   ├── heuristics.cpython-310.pyc
│   │       │   │   │   │   ├── serialize.cpython-310.pyc
│   │       │   │   │   │   └── wrapper.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── caches\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   │   ├── file_cache.cpython-310.pyc
│   │       │   │   │   │   │   └── redis_cache.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── file_cache.py
│   │       │   │   │   │   └── redis_cache.py
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _cmd.py
│   │       │   │   │   ├── adapter.py
│   │       │   │   │   ├── cache.py
│   │       │   │   │   ├── compat.py
│   │       │   │   │   ├── controller.py
│   │       │   │   │   ├── filewrapper.py
│   │       │   │   │   ├── heuristics.py
│   │       │   │   │   ├── serialize.py
│   │       │   │   │   └── wrapper.py
│   │       │   │   │
│   │       │   │   ├── certifi\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── __main__.cpython-310.pyc
│   │       │   │   │   │   └── core.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── __main__.py
│   │       │   │   │   ├── cacert.pem
│   │       │   │   │   └── core.py
│   │       │   │   │
│   │       │   │   ├── chardet\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── big5freq.cpython-310.pyc
│   │       │   │   │   │   ├── big5prober.cpython-310.pyc
│   │       │   │   │   │   ├── chardistribution.cpython-310.pyc
│   │       │   │   │   │   ├── charsetgroupprober.cpython-310.pyc
│   │       │   │   │   │   ├── charsetprober.cpython-310.pyc
│   │       │   │   │   │   ├── codingstatemachine.cpython-310.pyc
│   │       │   │   │   │   ├── codingstatemachinedict.cpython-310.pyc
│   │       │   │   │   │   ├── cp949prober.cpython-310.pyc
│   │       │   │   │   │   ├── enums.cpython-310.pyc
│   │       │   │   │   │   ├── escprober.cpython-310.pyc
│   │       │   │   │   │   ├── escsm.cpython-310.pyc
│   │       │   │   │   │   ├── eucjpprober.cpython-310.pyc
│   │       │   │   │   │   ├── euckrfreq.cpython-310.pyc
│   │       │   │   │   │   ├── euckrprober.cpython-310.pyc
│   │       │   │   │   │   ├── euctwfreq.cpython-310.pyc
│   │       │   │   │   │   ├── euctwprober.cpython-310.pyc
│   │       │   │   │   │   ├── gb2312freq.cpython-310.pyc
│   │       │   │   │   │   ├── gb2312prober.cpython-310.pyc
│   │       │   │   │   │   ├── hebrewprober.cpython-310.pyc
│   │       │   │   │   │   ├── jisfreq.cpython-310.pyc
│   │       │   │   │   │   ├── johabfreq.cpython-310.pyc
│   │       │   │   │   │   ├── johabprober.cpython-310.pyc
│   │       │   │   │   │   ├── jpcntx.cpython-310.pyc
│   │       │   │   │   │   ├── langbulgarianmodel.cpython-310.pyc
│   │       │   │   │   │   ├── langgreekmodel.cpython-310.pyc
│   │       │   │   │   │   ├── langhebrewmodel.cpython-310.pyc
│   │       │   │   │   │   ├── langhungarianmodel.cpython-310.pyc
│   │       │   │   │   │   ├── langrussianmodel.cpython-310.pyc
│   │       │   │   │   │   ├── langthaimodel.cpython-310.pyc
│   │       │   │   │   │   ├── langturkishmodel.cpython-310.pyc
│   │       │   │   │   │   ├── latin1prober.cpython-310.pyc
│   │       │   │   │   │   ├── macromanprober.cpython-310.pyc
│   │       │   │   │   │   ├── mbcharsetprober.cpython-310.pyc
│   │       │   │   │   │   ├── mbcsgroupprober.cpython-310.pyc
│   │       │   │   │   │   ├── mbcssm.cpython-310.pyc
│   │       │   │   │   │   ├── resultdict.cpython-310.pyc
│   │       │   │   │   │   ├── sbcharsetprober.cpython-310.pyc
│   │       │   │   │   │   ├── sbcsgroupprober.cpython-310.pyc
│   │       │   │   │   │   ├── sjisprober.cpython-310.pyc
│   │       │   │   │   │   ├── universaldetector.cpython-310.pyc
│   │       │   │   │   │   ├── utf1632prober.cpython-310.pyc
│   │       │   │   │   │   ├── utf8prober.cpython-310.pyc
│   │       │   │   │   │   └── version.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── cli\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   │   └── chardetect.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   └── chardetect.py
│   │       │   │   │   │
│   │       │   │   │   ├── metadata\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   │   └── languages.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   └── languages.py
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── big5freq.py
│   │       │   │   │   ├── big5prober.py
│   │       │   │   │   ├── chardistribution.py
│   │       │   │   │   ├── charsetgroupprober.py
│   │       │   │   │   ├── charsetprober.py
│   │       │   │   │   ├── codingstatemachine.py
│   │       │   │   │   ├── codingstatemachinedict.py
│   │       │   │   │   ├── cp949prober.py
│   │       │   │   │   ├── enums.py
│   │       │   │   │   ├── escprober.py
│   │       │   │   │   ├── escsm.py
│   │       │   │   │   ├── eucjpprober.py
│   │       │   │   │   ├── euckrfreq.py
│   │       │   │   │   ├── euckrprober.py
│   │       │   │   │   ├── euctwfreq.py
│   │       │   │   │   ├── euctwprober.py
│   │       │   │   │   ├── gb2312freq.py
│   │       │   │   │   ├── gb2312prober.py
│   │       │   │   │   ├── hebrewprober.py
│   │       │   │   │   ├── jisfreq.py
│   │       │   │   │   ├── johabfreq.py
│   │       │   │   │   ├── johabprober.py
│   │       │   │   │   ├── jpcntx.py
│   │       │   │   │   ├── langbulgarianmodel.py
│   │       │   │   │   ├── langgreekmodel.py
│   │       │   │   │   ├── langhebrewmodel.py
│   │       │   │   │   ├── langhungarianmodel.py
│   │       │   │   │   ├── langrussianmodel.py
│   │       │   │   │   ├── langthaimodel.py
│   │       │   │   │   ├── langturkishmodel.py
│   │       │   │   │   ├── latin1prober.py
│   │       │   │   │   ├── macromanprober.py
│   │       │   │   │   ├── mbcharsetprober.py
│   │       │   │   │   ├── mbcsgroupprober.py
│   │       │   │   │   ├── mbcssm.py
│   │       │   │   │   ├── resultdict.py
│   │       │   │   │   ├── sbcharsetprober.py
│   │       │   │   │   ├── sbcsgroupprober.py
│   │       │   │   │   ├── sjisprober.py
│   │       │   │   │   ├── universaldetector.py
│   │       │   │   │   ├── utf1632prober.py
│   │       │   │   │   ├── utf8prober.py
│   │       │   │   │   └── version.py
│   │       │   │   │
│   │       │   │   ├── colorama\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── ansi.cpython-310.pyc
│   │       │   │   │   │   ├── ansitowin32.cpython-310.pyc
│   │       │   │   │   │   ├── initialise.cpython-310.pyc
│   │       │   │   │   │   ├── win32.cpython-310.pyc
│   │       │   │   │   │   └── winterm.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── tests\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   │   ├── ansi_test.cpython-310.pyc
│   │       │   │   │   │   │   ├── ansitowin32_test.cpython-310.pyc
│   │       │   │   │   │   │   ├── initialise_test.cpython-310.pyc
│   │       │   │   │   │   │   ├── isatty_test.cpython-310.pyc
│   │       │   │   │   │   │   ├── utils.cpython-310.pyc
│   │       │   │   │   │   │   └── winterm_test.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── ansi_test.py
│   │       │   │   │   │   ├── ansitowin32_test.py
│   │       │   │   │   │   ├── initialise_test.py
│   │       │   │   │   │   ├── isatty_test.py
│   │       │   │   │   │   ├── utils.py
│   │       │   │   │   │   └── winterm_test.py
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── ansi.py
│   │       │   │   │   ├── ansitowin32.py
│   │       │   │   │   ├── initialise.py
│   │       │   │   │   ├── win32.py
│   │       │   │   │   └── winterm.py
│   │       │   │   │
│   │       │   │   ├── distlib\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── compat.cpython-310.pyc
│   │       │   │   │   │   ├── database.cpython-310.pyc
│   │       │   │   │   │   ├── index.cpython-310.pyc
│   │       │   │   │   │   ├── locators.cpython-310.pyc
│   │       │   │   │   │   ├── manifest.cpython-310.pyc
│   │       │   │   │   │   ├── markers.cpython-310.pyc
│   │       │   │   │   │   ├── metadata.cpython-310.pyc
│   │       │   │   │   │   ├── resources.cpython-310.pyc
│   │       │   │   │   │   ├── scripts.cpython-310.pyc
│   │       │   │   │   │   ├── util.cpython-310.pyc
│   │       │   │   │   │   ├── version.cpython-310.pyc
│   │       │   │   │   │   └── wheel.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── compat.py
│   │       │   │   │   ├── database.py
│   │       │   │   │   ├── index.py
│   │       │   │   │   ├── locators.py
│   │       │   │   │   ├── manifest.py
│   │       │   │   │   ├── markers.py
│   │       │   │   │   ├── metadata.py
│   │       │   │   │   ├── resources.py
│   │       │   │   │   ├── scripts.py
│   │       │   │   │   ├── t32.exe
│   │       │   │   │   ├── t64-arm.exe
│   │       │   │   │   ├── t64.exe
│   │       │   │   │   ├── util.py
│   │       │   │   │   ├── version.py
│   │       │   │   │   ├── w32.exe
│   │       │   │   │   ├── w64-arm.exe
│   │       │   │   │   ├── w64.exe
│   │       │   │   │   └── wheel.py
│   │       │   │   │
│   │       │   │   ├── distro\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── __main__.cpython-310.pyc
│   │       │   │   │   │   └── distro.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── __main__.py
│   │       │   │   │   └── distro.py
│   │       │   │   │
│   │       │   │   ├── idna\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── codec.cpython-310.pyc
│   │       │   │   │   │   ├── compat.cpython-310.pyc
│   │       │   │   │   │   ├── core.cpython-310.pyc
│   │       │   │   │   │   ├── idnadata.cpython-310.pyc
│   │       │   │   │   │   ├── intranges.cpython-310.pyc
│   │       │   │   │   │   ├── package_data.cpython-310.pyc
│   │       │   │   │   │   └── uts46data.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── codec.py
│   │       │   │   │   ├── compat.py
│   │       │   │   │   ├── core.py
│   │       │   │   │   ├── idnadata.py
│   │       │   │   │   ├── intranges.py
│   │       │   │   │   ├── package_data.py
│   │       │   │   │   └── uts46data.py
│   │       │   │   │
│   │       │   │   ├── msgpack\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── exceptions.cpython-310.pyc
│   │       │   │   │   │   ├── ext.cpython-310.pyc
│   │       │   │   │   │   └── fallback.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── exceptions.py
│   │       │   │   │   ├── ext.py
│   │       │   │   │   └── fallback.py
│   │       │   │   │
│   │       │   │   ├── packaging\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __about__.cpython-310.pyc
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── _manylinux.cpython-310.pyc
│   │       │   │   │   │   ├── _musllinux.cpython-310.pyc
│   │       │   │   │   │   ├── _structures.cpython-310.pyc
│   │       │   │   │   │   ├── markers.cpython-310.pyc
│   │       │   │   │   │   ├── requirements.cpython-310.pyc
│   │       │   │   │   │   ├── specifiers.cpython-310.pyc
│   │       │   │   │   │   ├── tags.cpython-310.pyc
│   │       │   │   │   │   ├── utils.cpython-310.pyc
│   │       │   │   │   │   └── version.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __about__.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _manylinux.py
│   │       │   │   │   ├── _musllinux.py
│   │       │   │   │   ├── _structures.py
│   │       │   │   │   ├── markers.py
│   │       │   │   │   ├── requirements.py
│   │       │   │   │   ├── specifiers.py
│   │       │   │   │   ├── tags.py
│   │       │   │   │   ├── utils.py
│   │       │   │   │   └── version.py
│   │       │   │   │
│   │       │   │   ├── pkg_resources\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   └── py31compat.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   └── py31compat.py
│   │       │   │   │
│   │       │   │   ├── platformdirs\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── __main__.cpython-310.pyc
│   │       │   │   │   │   ├── android.cpython-310.pyc
│   │       │   │   │   │   ├── api.cpython-310.pyc
│   │       │   │   │   │   ├── macos.cpython-310.pyc
│   │       │   │   │   │   ├── unix.cpython-310.pyc
│   │       │   │   │   │   ├── version.cpython-310.pyc
│   │       │   │   │   │   └── windows.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── __main__.py
│   │       │   │   │   ├── android.py
│   │       │   │   │   ├── api.py
│   │       │   │   │   ├── macos.py
│   │       │   │   │   ├── unix.py
│   │       │   │   │   ├── version.py
│   │       │   │   │   └── windows.py
│   │       │   │   │
│   │       │   │   ├── pygments\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── __main__.cpython-310.pyc
│   │       │   │   │   │   ├── cmdline.cpython-310.pyc
│   │       │   │   │   │   ├── console.cpython-310.pyc
│   │       │   │   │   │   ├── filter.cpython-310.pyc
│   │       │   │   │   │   ├── formatter.cpython-310.pyc
│   │       │   │   │   │   ├── lexer.cpython-310.pyc
│   │       │   │   │   │   ├── modeline.cpython-310.pyc
│   │       │   │   │   │   ├── plugin.cpython-310.pyc
│   │       │   │   │   │   ├── regexopt.cpython-310.pyc
│   │       │   │   │   │   ├── scanner.cpython-310.pyc
│   │       │   │   │   │   ├── sphinxext.cpython-310.pyc
│   │       │   │   │   │   ├── style.cpython-310.pyc
│   │       │   │   │   │   ├── token.cpython-310.pyc
│   │       │   │   │   │   ├── unistring.cpython-310.pyc
│   │       │   │   │   │   └── util.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── filters\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   └── __init__.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   └── __init__.py
│   │       │   │   │   │
│   │       │   │   │   ├── formatters\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   │   ├── _mapping.cpython-310.pyc
│   │       │   │   │   │   │   ├── bbcode.cpython-310.pyc
│   │       │   │   │   │   │   ├── groff.cpython-310.pyc
│   │       │   │   │   │   │   ├── html.cpython-310.pyc
│   │       │   │   │   │   │   ├── img.cpython-310.pyc
│   │       │   │   │   │   │   ├── irc.cpython-310.pyc
│   │       │   │   │   │   │   ├── latex.cpython-310.pyc
│   │       │   │   │   │   │   ├── other.cpython-310.pyc
│   │       │   │   │   │   │   ├── pangomarkup.cpython-310.pyc
│   │       │   │   │   │   │   ├── rtf.cpython-310.pyc
│   │       │   │   │   │   │   ├── svg.cpython-310.pyc
│   │       │   │   │   │   │   ├── terminal.cpython-310.pyc
│   │       │   │   │   │   │   └── terminal256.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── _mapping.py
│   │       │   │   │   │   ├── bbcode.py
│   │       │   │   │   │   ├── groff.py
│   │       │   │   │   │   ├── html.py
│   │       │   │   │   │   ├── img.py
│   │       │   │   │   │   ├── irc.py
│   │       │   │   │   │   ├── latex.py
│   │       │   │   │   │   ├── other.py
│   │       │   │   │   │   ├── pangomarkup.py
│   │       │   │   │   │   ├── rtf.py
│   │       │   │   │   │   ├── svg.py
│   │       │   │   │   │   ├── terminal.py
│   │       │   │   │   │   └── terminal256.py
│   │       │   │   │   │
│   │       │   │   │   ├── lexers\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   │   ├── _mapping.cpython-310.pyc
│   │       │   │   │   │   │   └── python.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── _mapping.py
│   │       │   │   │   │   └── python.py
│   │       │   │   │   │
│   │       │   │   │   ├── styles\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   └── __init__.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   └── __init__.py
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── __main__.py
│   │       │   │   │   ├── cmdline.py
│   │       │   │   │   ├── console.py
│   │       │   │   │   ├── filter.py
│   │       │   │   │   ├── formatter.py
│   │       │   │   │   ├── lexer.py
│   │       │   │   │   ├── modeline.py
│   │       │   │   │   ├── plugin.py
│   │       │   │   │   ├── regexopt.py
│   │       │   │   │   ├── scanner.py
│   │       │   │   │   ├── sphinxext.py
│   │       │   │   │   ├── style.py
│   │       │   │   │   ├── token.py
│   │       │   │   │   ├── unistring.py
│   │       │   │   │   └── util.py
│   │       │   │   │
│   │       │   │   ├── pyparsing\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── actions.cpython-310.pyc
│   │       │   │   │   │   ├── common.cpython-310.pyc
│   │       │   │   │   │   ├── core.cpython-310.pyc
│   │       │   │   │   │   ├── exceptions.cpython-310.pyc
│   │       │   │   │   │   ├── helpers.cpython-310.pyc
│   │       │   │   │   │   ├── results.cpython-310.pyc
│   │       │   │   │   │   ├── testing.cpython-310.pyc
│   │       │   │   │   │   ├── unicode.cpython-310.pyc
│   │       │   │   │   │   └── util.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── diagram\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   └── __init__.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   └── __init__.py
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── actions.py
│   │       │   │   │   ├── common.py
│   │       │   │   │   ├── core.py
│   │       │   │   │   ├── exceptions.py
│   │       │   │   │   ├── helpers.py
│   │       │   │   │   ├── results.py
│   │       │   │   │   ├── testing.py
│   │       │   │   │   ├── unicode.py
│   │       │   │   │   └── util.py
│   │       │   │   │
│   │       │   │   ├── pyproject_hooks\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── _compat.cpython-310.pyc
│   │       │   │   │   │   └── _impl.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── _in_process\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   │   └── _in_process.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   └── _in_process.py
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _compat.py
│   │       │   │   │   └── _impl.py
│   │       │   │   │
│   │       │   │   ├── requests\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── __version__.cpython-310.pyc
│   │       │   │   │   │   ├── _internal_utils.cpython-310.pyc
│   │       │   │   │   │   ├── adapters.cpython-310.pyc
│   │       │   │   │   │   ├── api.cpython-310.pyc
│   │       │   │   │   │   ├── auth.cpython-310.pyc
│   │       │   │   │   │   ├── certs.cpython-310.pyc
│   │       │   │   │   │   ├── compat.cpython-310.pyc
│   │       │   │   │   │   ├── cookies.cpython-310.pyc
│   │       │   │   │   │   ├── exceptions.cpython-310.pyc
│   │       │   │   │   │   ├── help.cpython-310.pyc
│   │       │   │   │   │   ├── hooks.cpython-310.pyc
│   │       │   │   │   │   ├── models.cpython-310.pyc
│   │       │   │   │   │   ├── packages.cpython-310.pyc
│   │       │   │   │   │   ├── sessions.cpython-310.pyc
│   │       │   │   │   │   ├── status_codes.cpython-310.pyc
│   │       │   │   │   │   ├── structures.cpython-310.pyc
│   │       │   │   │   │   └── utils.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── __version__.py
│   │       │   │   │   ├── _internal_utils.py
│   │       │   │   │   ├── adapters.py
│   │       │   │   │   ├── api.py
│   │       │   │   │   ├── auth.py
│   │       │   │   │   ├── certs.py
│   │       │   │   │   ├── compat.py
│   │       │   │   │   ├── cookies.py
│   │       │   │   │   ├── exceptions.py
│   │       │   │   │   ├── help.py
│   │       │   │   │   ├── hooks.py
│   │       │   │   │   ├── models.py
│   │       │   │   │   ├── packages.py
│   │       │   │   │   ├── sessions.py
│   │       │   │   │   ├── status_codes.py
│   │       │   │   │   ├── structures.py
│   │       │   │   │   └── utils.py
│   │       │   │   │
│   │       │   │   ├── resolvelib\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── providers.cpython-310.pyc
│   │       │   │   │   │   ├── reporters.cpython-310.pyc
│   │       │   │   │   │   ├── resolvers.cpython-310.pyc
│   │       │   │   │   │   └── structs.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── compat\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   │   └── collections_abc.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   └── collections_abc.py
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── providers.py
│   │       │   │   │   ├── reporters.py
│   │       │   │   │   ├── resolvers.py
│   │       │   │   │   └── structs.py
│   │       │   │   │
│   │       │   │   ├── rich\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── __main__.cpython-310.pyc
│   │       │   │   │   │   ├── _cell_widths.cpython-310.pyc
│   │       │   │   │   │   ├── _emoji_codes.cpython-310.pyc
│   │       │   │   │   │   ├── _emoji_replace.cpython-310.pyc
│   │       │   │   │   │   ├── _export_format.cpython-310.pyc
│   │       │   │   │   │   ├── _extension.cpython-310.pyc
│   │       │   │   │   │   ├── _inspect.cpython-310.pyc
│   │       │   │   │   │   ├── _log_render.cpython-310.pyc
│   │       │   │   │   │   ├── _loop.cpython-310.pyc
│   │       │   │   │   │   ├── _null_file.cpython-310.pyc
│   │       │   │   │   │   ├── _palettes.cpython-310.pyc
│   │       │   │   │   │   ├── _pick.cpython-310.pyc
│   │       │   │   │   │   ├── _ratio.cpython-310.pyc
│   │       │   │   │   │   ├── _spinners.cpython-310.pyc
│   │       │   │   │   │   ├── _stack.cpython-310.pyc
│   │       │   │   │   │   ├── _timer.cpython-310.pyc
│   │       │   │   │   │   ├── _win32_console.cpython-310.pyc
│   │       │   │   │   │   ├── _windows.cpython-310.pyc
│   │       │   │   │   │   ├── _windows_renderer.cpython-310.pyc
│   │       │   │   │   │   ├── _wrap.cpython-310.pyc
│   │       │   │   │   │   ├── abc.cpython-310.pyc
│   │       │   │   │   │   ├── align.cpython-310.pyc
│   │       │   │   │   │   ├── ansi.cpython-310.pyc
│   │       │   │   │   │   ├── bar.cpython-310.pyc
│   │       │   │   │   │   ├── box.cpython-310.pyc
│   │       │   │   │   │   ├── cells.cpython-310.pyc
│   │       │   │   │   │   ├── color.cpython-310.pyc
│   │       │   │   │   │   ├── color_triplet.cpython-310.pyc
│   │       │   │   │   │   ├── columns.cpython-310.pyc
│   │       │   │   │   │   ├── console.cpython-310.pyc
│   │       │   │   │   │   ├── constrain.cpython-310.pyc
│   │       │   │   │   │   ├── containers.cpython-310.pyc
│   │       │   │   │   │   ├── control.cpython-310.pyc
│   │       │   │   │   │   ├── default_styles.cpython-310.pyc
│   │       │   │   │   │   ├── diagnose.cpython-310.pyc
│   │       │   │   │   │   ├── emoji.cpython-310.pyc
│   │       │   │   │   │   ├── errors.cpython-310.pyc
│   │       │   │   │   │   ├── file_proxy.cpython-310.pyc
│   │       │   │   │   │   ├── filesize.cpython-310.pyc
│   │       │   │   │   │   ├── highlighter.cpython-310.pyc
│   │       │   │   │   │   ├── json.cpython-310.pyc
│   │       │   │   │   │   ├── jupyter.cpython-310.pyc
│   │       │   │   │   │   ├── layout.cpython-310.pyc
│   │       │   │   │   │   ├── live.cpython-310.pyc
│   │       │   │   │   │   ├── live_render.cpython-310.pyc
│   │       │   │   │   │   ├── logging.cpython-310.pyc
│   │       │   │   │   │   ├── markup.cpython-310.pyc
│   │       │   │   │   │   ├── measure.cpython-310.pyc
│   │       │   │   │   │   ├── padding.cpython-310.pyc
│   │       │   │   │   │   ├── pager.cpython-310.pyc
│   │       │   │   │   │   ├── palette.cpython-310.pyc
│   │       │   │   │   │   ├── panel.cpython-310.pyc
│   │       │   │   │   │   ├── pretty.cpython-310.pyc
│   │       │   │   │   │   ├── progress.cpython-310.pyc
│   │       │   │   │   │   ├── progress_bar.cpython-310.pyc
│   │       │   │   │   │   ├── prompt.cpython-310.pyc
│   │       │   │   │   │   ├── protocol.cpython-310.pyc
│   │       │   │   │   │   ├── region.cpython-310.pyc
│   │       │   │   │   │   ├── repr.cpython-310.pyc
│   │       │   │   │   │   ├── rule.cpython-310.pyc
│   │       │   │   │   │   ├── scope.cpython-310.pyc
│   │       │   │   │   │   ├── screen.cpython-310.pyc
│   │       │   │   │   │   ├── segment.cpython-310.pyc
│   │       │   │   │   │   ├── spinner.cpython-310.pyc
│   │       │   │   │   │   ├── status.cpython-310.pyc
│   │       │   │   │   │   ├── style.cpython-310.pyc
│   │       │   │   │   │   ├── styled.cpython-310.pyc
│   │       │   │   │   │   ├── syntax.cpython-310.pyc
│   │       │   │   │   │   ├── table.cpython-310.pyc
│   │       │   │   │   │   ├── terminal_theme.cpython-310.pyc
│   │       │   │   │   │   ├── text.cpython-310.pyc
│   │       │   │   │   │   ├── theme.cpython-310.pyc
│   │       │   │   │   │   ├── themes.cpython-310.pyc
│   │       │   │   │   │   ├── traceback.cpython-310.pyc
│   │       │   │   │   │   └── tree.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── __main__.py
│   │       │   │   │   ├── _cell_widths.py
│   │       │   │   │   ├── _emoji_codes.py
│   │       │   │   │   ├── _emoji_replace.py
│   │       │   │   │   ├── _export_format.py
│   │       │   │   │   ├── _extension.py
│   │       │   │   │   ├── _inspect.py
│   │       │   │   │   ├── _log_render.py
│   │       │   │   │   ├── _loop.py
│   │       │   │   │   ├── _null_file.py
│   │       │   │   │   ├── _palettes.py
│   │       │   │   │   ├── _pick.py
│   │       │   │   │   ├── _ratio.py
│   │       │   │   │   ├── _spinners.py
│   │       │   │   │   ├── _stack.py
│   │       │   │   │   ├── _timer.py
│   │       │   │   │   ├── _win32_console.py
│   │       │   │   │   ├── _windows.py
│   │       │   │   │   ├── _windows_renderer.py
│   │       │   │   │   ├── _wrap.py
│   │       │   │   │   ├── abc.py
│   │       │   │   │   ├── align.py
│   │       │   │   │   ├── ansi.py
│   │       │   │   │   ├── bar.py
│   │       │   │   │   ├── box.py
│   │       │   │   │   ├── cells.py
│   │       │   │   │   ├── color.py
│   │       │   │   │   ├── color_triplet.py
│   │       │   │   │   ├── columns.py
│   │       │   │   │   ├── console.py
│   │       │   │   │   ├── constrain.py
│   │       │   │   │   ├── containers.py
│   │       │   │   │   ├── control.py
│   │       │   │   │   ├── default_styles.py
│   │       │   │   │   ├── diagnose.py
│   │       │   │   │   ├── emoji.py
│   │       │   │   │   ├── errors.py
│   │       │   │   │   ├── file_proxy.py
│   │       │   │   │   ├── filesize.py
│   │       │   │   │   ├── highlighter.py
│   │       │   │   │   ├── json.py
│   │       │   │   │   ├── jupyter.py
│   │       │   │   │   ├── layout.py
│   │       │   │   │   ├── live.py
│   │       │   │   │   ├── live_render.py
│   │       │   │   │   ├── logging.py
│   │       │   │   │   ├── markup.py
│   │       │   │   │   ├── measure.py
│   │       │   │   │   ├── padding.py
│   │       │   │   │   ├── pager.py
│   │       │   │   │   ├── palette.py
│   │       │   │   │   ├── panel.py
│   │       │   │   │   ├── pretty.py
│   │       │   │   │   ├── progress.py
│   │       │   │   │   ├── progress_bar.py
│   │       │   │   │   ├── prompt.py
│   │       │   │   │   ├── protocol.py
│   │       │   │   │   ├── region.py
│   │       │   │   │   ├── repr.py
│   │       │   │   │   ├── rule.py
│   │       │   │   │   ├── scope.py
│   │       │   │   │   ├── screen.py
│   │       │   │   │   ├── segment.py
│   │       │   │   │   ├── spinner.py
│   │       │   │   │   ├── status.py
│   │       │   │   │   ├── style.py
│   │       │   │   │   ├── styled.py
│   │       │   │   │   ├── syntax.py
│   │       │   │   │   ├── table.py
│   │       │   │   │   ├── terminal_theme.py
│   │       │   │   │   ├── text.py
│   │       │   │   │   ├── theme.py
│   │       │   │   │   ├── themes.py
│   │       │   │   │   ├── traceback.py
│   │       │   │   │   └── tree.py
│   │       │   │   │
│   │       │   │   ├── tenacity\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── _asyncio.cpython-310.pyc
│   │       │   │   │   │   ├── _utils.cpython-310.pyc
│   │       │   │   │   │   ├── after.cpython-310.pyc
│   │       │   │   │   │   ├── before.cpython-310.pyc
│   │       │   │   │   │   ├── before_sleep.cpython-310.pyc
│   │       │   │   │   │   ├── nap.cpython-310.pyc
│   │       │   │   │   │   ├── retry.cpython-310.pyc
│   │       │   │   │   │   ├── stop.cpython-310.pyc
│   │       │   │   │   │   ├── tornadoweb.cpython-310.pyc
│   │       │   │   │   │   └── wait.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _asyncio.py
│   │       │   │   │   ├── _utils.py
│   │       │   │   │   ├── after.py
│   │       │   │   │   ├── before.py
│   │       │   │   │   ├── before_sleep.py
│   │       │   │   │   ├── nap.py
│   │       │   │   │   ├── retry.py
│   │       │   │   │   ├── stop.py
│   │       │   │   │   ├── tornadoweb.py
│   │       │   │   │   └── wait.py
│   │       │   │   │
│   │       │   │   ├── tomli\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── _parser.cpython-310.pyc
│   │       │   │   │   │   ├── _re.cpython-310.pyc
│   │       │   │   │   │   └── _types.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _parser.py
│   │       │   │   │   ├── _re.py
│   │       │   │   │   └── _types.py
│   │       │   │   │
│   │       │   │   ├── urllib3\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── _collections.cpython-310.pyc
│   │       │   │   │   │   ├── _version.cpython-310.pyc
│   │       │   │   │   │   ├── connection.cpython-310.pyc
│   │       │   │   │   │   ├── connectionpool.cpython-310.pyc
│   │       │   │   │   │   ├── exceptions.cpython-310.pyc
│   │       │   │   │   │   ├── fields.cpython-310.pyc
│   │       │   │   │   │   ├── filepost.cpython-310.pyc
│   │       │   │   │   │   ├── poolmanager.cpython-310.pyc
│   │       │   │   │   │   ├── request.cpython-310.pyc
│   │       │   │   │   │   └── response.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── contrib\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   │   ├── _appengine_environ.cpython-310.pyc
│   │       │   │   │   │   │   ├── appengine.cpython-310.pyc
│   │       │   │   │   │   │   ├── ntlmpool.cpython-310.pyc
│   │       │   │   │   │   │   ├── pyopenssl.cpython-310.pyc
│   │       │   │   │   │   │   ├── securetransport.cpython-310.pyc
│   │       │   │   │   │   │   └── socks.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── _securetransport\
│   │       │   │   │   │   │   │
│   │       │   │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   │   │   ├── bindings.cpython-310.pyc
│   │       │   │   │   │   │   │   └── low_level.cpython-310.pyc
│   │       │   │   │   │   │   │
│   │       │   │   │   │   │   ├── __init__.py
│   │       │   │   │   │   │   ├── bindings.py
│   │       │   │   │   │   │   └── low_level.py
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── _appengine_environ.py
│   │       │   │   │   │   ├── appengine.py
│   │       │   │   │   │   ├── ntlmpool.py
│   │       │   │   │   │   ├── pyopenssl.py
│   │       │   │   │   │   ├── securetransport.py
│   │       │   │   │   │   └── socks.py
│   │       │   │   │   │
│   │       │   │   │   ├── packages\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   │   └── six.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── backports\
│   │       │   │   │   │   │   │
│   │       │   │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   │   │   └── makefile.cpython-310.pyc
│   │       │   │   │   │   │   │
│   │       │   │   │   │   │   ├── __init__.py
│   │       │   │   │   │   │   └── makefile.py
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   └── six.py
│   │       │   │   │   │
│   │       │   │   │   ├── util\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   │   ├── connection.cpython-310.pyc
│   │       │   │   │   │   │   ├── proxy.cpython-310.pyc
│   │       │   │   │   │   │   ├── queue.cpython-310.pyc
│   │       │   │   │   │   │   ├── request.cpython-310.pyc
│   │       │   │   │   │   │   ├── response.cpython-310.pyc
│   │       │   │   │   │   │   ├── retry.cpython-310.pyc
│   │       │   │   │   │   │   ├── ssl_.cpython-310.pyc
│   │       │   │   │   │   │   ├── ssl_match_hostname.cpython-310.pyc
│   │       │   │   │   │   │   ├── ssltransport.cpython-310.pyc
│   │       │   │   │   │   │   ├── timeout.cpython-310.pyc
│   │       │   │   │   │   │   ├── url.cpython-310.pyc
│   │       │   │   │   │   │   └── wait.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── connection.py
│   │       │   │   │   │   ├── proxy.py
│   │       │   │   │   │   ├── queue.py
│   │       │   │   │   │   ├── request.py
│   │       │   │   │   │   ├── response.py
│   │       │   │   │   │   ├── retry.py
│   │       │   │   │   │   ├── ssl_.py
│   │       │   │   │   │   ├── ssl_match_hostname.py
│   │       │   │   │   │   ├── ssltransport.py
│   │       │   │   │   │   ├── timeout.py
│   │       │   │   │   │   ├── url.py
│   │       │   │   │   │   └── wait.py
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _collections.py
│   │       │   │   │   ├── _version.py
│   │       │   │   │   ├── connection.py
│   │       │   │   │   ├── connectionpool.py
│   │       │   │   │   ├── exceptions.py
│   │       │   │   │   ├── fields.py
│   │       │   │   │   ├── filepost.py
│   │       │   │   │   ├── poolmanager.py
│   │       │   │   │   ├── request.py
│   │       │   │   │   └── response.py
│   │       │   │   │
│   │       │   │   ├── webencodings\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── labels.cpython-310.pyc
│   │       │   │   │   │   ├── mklabels.cpython-310.pyc
│   │       │   │   │   │   ├── tests.cpython-310.pyc
│   │       │   │   │   │   └── x_user_defined.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── labels.py
│   │       │   │   │   ├── mklabels.py
│   │       │   │   │   ├── tests.py
│   │       │   │   │   └── x_user_defined.py
│   │       │   │   │
│   │       │   │   ├── __init__.py
│   │       │   │   ├── six.py
│   │       │   │   ├── typing_extensions.py
│   │       │   │   └── vendor.txt
│   │       │   │
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── __pip-runner__.py
│   │       │   └── py.typed
│   │       │
│   │       ├── pip-23.0.1.dist-info\
│   │       │   ├── INSTALLER
│   │       │   ├── LICENSE.txt
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   ├── REQUESTED
│   │       │   ├── WHEEL
│   │       │   ├── entry_points.txt
│   │       │   └── top_level.txt
│   │       │
│   │       ├── pkg_resources\
│   │       │   │
│   │       │   ├── __pycache__\
│   │       │   │   └── __init__.cpython-310.pyc
│   │       │   │
│   │       │   ├── _vendor\
│   │       │   │   │
│   │       │   │   ├── __pycache__\
│   │       │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   ├── appdirs.cpython-310.pyc
│   │       │   │   │   └── zipp.cpython-310.pyc
│   │       │   │   │
│   │       │   │   ├── importlib_resources\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── _adapters.cpython-310.pyc
│   │       │   │   │   │   ├── _common.cpython-310.pyc
│   │       │   │   │   │   ├── _compat.cpython-310.pyc
│   │       │   │   │   │   ├── _itertools.cpython-310.pyc
│   │       │   │   │   │   ├── _legacy.cpython-310.pyc
│   │       │   │   │   │   ├── abc.cpython-310.pyc
│   │       │   │   │   │   ├── readers.cpython-310.pyc
│   │       │   │   │   │   └── simple.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _adapters.py
│   │       │   │   │   ├── _common.py
│   │       │   │   │   ├── _compat.py
│   │       │   │   │   ├── _itertools.py
│   │       │   │   │   ├── _legacy.py
│   │       │   │   │   ├── abc.py
│   │       │   │   │   ├── readers.py
│   │       │   │   │   └── simple.py
│   │       │   │   │
│   │       │   │   ├── jaraco\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── context.cpython-310.pyc
│   │       │   │   │   │   └── functools.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── text\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   └── __init__.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   └── __init__.py
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── context.py
│   │       │   │   │   └── functools.py
│   │       │   │   │
│   │       │   │   ├── more_itertools\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── more.cpython-310.pyc
│   │       │   │   │   │   └── recipes.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── more.py
│   │       │   │   │   └── recipes.py
│   │       │   │   │
│   │       │   │   ├── packaging\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __about__.cpython-310.pyc
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── _manylinux.cpython-310.pyc
│   │       │   │   │   │   ├── _musllinux.cpython-310.pyc
│   │       │   │   │   │   ├── _structures.cpython-310.pyc
│   │       │   │   │   │   ├── markers.cpython-310.pyc
│   │       │   │   │   │   ├── requirements.cpython-310.pyc
│   │       │   │   │   │   ├── specifiers.cpython-310.pyc
│   │       │   │   │   │   ├── tags.cpython-310.pyc
│   │       │   │   │   │   ├── utils.cpython-310.pyc
│   │       │   │   │   │   └── version.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __about__.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _manylinux.py
│   │       │   │   │   ├── _musllinux.py
│   │       │   │   │   ├── _structures.py
│   │       │   │   │   ├── markers.py
│   │       │   │   │   ├── requirements.py
│   │       │   │   │   ├── specifiers.py
│   │       │   │   │   ├── tags.py
│   │       │   │   │   ├── utils.py
│   │       │   │   │   └── version.py
│   │       │   │   │
│   │       │   │   ├── pyparsing\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── actions.cpython-310.pyc
│   │       │   │   │   │   ├── common.cpython-310.pyc
│   │       │   │   │   │   ├── core.cpython-310.pyc
│   │       │   │   │   │   ├── exceptions.cpython-310.pyc
│   │       │   │   │   │   ├── helpers.cpython-310.pyc
│   │       │   │   │   │   ├── results.cpython-310.pyc
│   │       │   │   │   │   ├── testing.cpython-310.pyc
│   │       │   │   │   │   ├── unicode.cpython-310.pyc
│   │       │   │   │   │   └── util.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── diagram\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   └── __init__.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   └── __init__.py
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── actions.py
│   │       │   │   │   ├── common.py
│   │       │   │   │   ├── core.py
│   │       │   │   │   ├── exceptions.py
│   │       │   │   │   ├── helpers.py
│   │       │   │   │   ├── results.py
│   │       │   │   │   ├── testing.py
│   │       │   │   │   ├── unicode.py
│   │       │   │   │   └── util.py
│   │       │   │   │
│   │       │   │   ├── __init__.py
│   │       │   │   ├── appdirs.py
│   │       │   │   └── zipp.py
│   │       │   │
│   │       │   ├── extern\
│   │       │   │   │
│   │       │   │   ├── __pycache__\
│   │       │   │   │   └── __init__.cpython-310.pyc
│   │       │   │   │
│   │       │   │   └── __init__.py
│   │       │   │
│   │       │   └── __init__.py
│   │       │
│   │       ├── rptree\
│   │       │   │
│   │       │   ├── __pycache__\
│   │       │   │   ├── __init__.cpython-310.pyc
│   │       │   │   ├── __main__.cpython-310.pyc
│   │       │   │   ├── cli.cpython-310.pyc
│   │       │   │   └── rptree.cpython-310.pyc
│   │       │   │
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── cli.py
│   │       │   └── rptree.py
│   │       │
│   │       ├── rptree-0.1.1.dist-info\
│   │       │   ├── INSTALLER
│   │       │   ├── LICENSE
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   ├── REQUESTED
│   │       │   ├── WHEEL
│   │       │   ├── entry_points.txt
│   │       │   └── top_level.txt
│   │       │
│   │       ├── setuptools\
│   │       │   │
│   │       │   ├── __pycache__\
│   │       │   │   ├── __init__.cpython-310.pyc
│   │       │   │   ├── _deprecation_warning.cpython-310.pyc
│   │       │   │   ├── _entry_points.cpython-310.pyc
│   │       │   │   ├── _imp.cpython-310.pyc
│   │       │   │   ├── _importlib.cpython-310.pyc
│   │       │   │   ├── _itertools.cpython-310.pyc
│   │       │   │   ├── _path.cpython-310.pyc
│   │       │   │   ├── _reqs.cpython-310.pyc
│   │       │   │   ├── archive_util.cpython-310.pyc
│   │       │   │   ├── build_meta.cpython-310.pyc
│   │       │   │   ├── dep_util.cpython-310.pyc
│   │       │   │   ├── depends.cpython-310.pyc
│   │       │   │   ├── discovery.cpython-310.pyc
│   │       │   │   ├── dist.cpython-310.pyc
│   │       │   │   ├── errors.cpython-310.pyc
│   │       │   │   ├── extension.cpython-310.pyc
│   │       │   │   ├── glob.cpython-310.pyc
│   │       │   │   ├── installer.cpython-310.pyc
│   │       │   │   ├── launch.cpython-310.pyc
│   │       │   │   ├── logging.cpython-310.pyc
│   │       │   │   ├── monkey.cpython-310.pyc
│   │       │   │   ├── msvc.cpython-310.pyc
│   │       │   │   ├── namespaces.cpython-310.pyc
│   │       │   │   ├── package_index.cpython-310.pyc
│   │       │   │   ├── py34compat.cpython-310.pyc
│   │       │   │   ├── sandbox.cpython-310.pyc
│   │       │   │   ├── unicode_utils.cpython-310.pyc
│   │       │   │   ├── version.cpython-310.pyc
│   │       │   │   ├── wheel.cpython-310.pyc
│   │       │   │   └── windows_support.cpython-310.pyc
│   │       │   │
│   │       │   ├── _distutils\
│   │       │   │   │
│   │       │   │   ├── __pycache__\
│   │       │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   ├── _collections.cpython-310.pyc
│   │       │   │   │   ├── _functools.cpython-310.pyc
│   │       │   │   │   ├── _macos_compat.cpython-310.pyc
│   │       │   │   │   ├── _msvccompiler.cpython-310.pyc
│   │       │   │   │   ├── archive_util.cpython-310.pyc
│   │       │   │   │   ├── bcppcompiler.cpython-310.pyc
│   │       │   │   │   ├── ccompiler.cpython-310.pyc
│   │       │   │   │   ├── cmd.cpython-310.pyc
│   │       │   │   │   ├── config.cpython-310.pyc
│   │       │   │   │   ├── core.cpython-310.pyc
│   │       │   │   │   ├── cygwinccompiler.cpython-310.pyc
│   │       │   │   │   ├── debug.cpython-310.pyc
│   │       │   │   │   ├── dep_util.cpython-310.pyc
│   │       │   │   │   ├── dir_util.cpython-310.pyc
│   │       │   │   │   ├── dist.cpython-310.pyc
│   │       │   │   │   ├── errors.cpython-310.pyc
│   │       │   │   │   ├── extension.cpython-310.pyc
│   │       │   │   │   ├── fancy_getopt.cpython-310.pyc
│   │       │   │   │   ├── file_util.cpython-310.pyc
│   │       │   │   │   ├── filelist.cpython-310.pyc
│   │       │   │   │   ├── log.cpython-310.pyc
│   │       │   │   │   ├── msvc9compiler.cpython-310.pyc
│   │       │   │   │   ├── msvccompiler.cpython-310.pyc
│   │       │   │   │   ├── py38compat.cpython-310.pyc
│   │       │   │   │   ├── py39compat.cpython-310.pyc
│   │       │   │   │   ├── spawn.cpython-310.pyc
│   │       │   │   │   ├── sysconfig.cpython-310.pyc
│   │       │   │   │   ├── text_file.cpython-310.pyc
│   │       │   │   │   ├── unixccompiler.cpython-310.pyc
│   │       │   │   │   ├── util.cpython-310.pyc
│   │       │   │   │   ├── version.cpython-310.pyc
│   │       │   │   │   └── versionpredicate.cpython-310.pyc
│   │       │   │   │
│   │       │   │   ├── command\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── _framework_compat.cpython-310.pyc
│   │       │   │   │   │   ├── bdist.cpython-310.pyc
│   │       │   │   │   │   ├── bdist_dumb.cpython-310.pyc
│   │       │   │   │   │   ├── bdist_rpm.cpython-310.pyc
│   │       │   │   │   │   ├── build.cpython-310.pyc
│   │       │   │   │   │   ├── build_clib.cpython-310.pyc
│   │       │   │   │   │   ├── build_ext.cpython-310.pyc
│   │       │   │   │   │   ├── build_py.cpython-310.pyc
│   │       │   │   │   │   ├── build_scripts.cpython-310.pyc
│   │       │   │   │   │   ├── check.cpython-310.pyc
│   │       │   │   │   │   ├── clean.cpython-310.pyc
│   │       │   │   │   │   ├── config.cpython-310.pyc
│   │       │   │   │   │   ├── install.cpython-310.pyc
│   │       │   │   │   │   ├── install_data.cpython-310.pyc
│   │       │   │   │   │   ├── install_egg_info.cpython-310.pyc
│   │       │   │   │   │   ├── install_headers.cpython-310.pyc
│   │       │   │   │   │   ├── install_lib.cpython-310.pyc
│   │       │   │   │   │   ├── install_scripts.cpython-310.pyc
│   │       │   │   │   │   ├── py37compat.cpython-310.pyc
│   │       │   │   │   │   ├── register.cpython-310.pyc
│   │       │   │   │   │   ├── sdist.cpython-310.pyc
│   │       │   │   │   │   └── upload.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _framework_compat.py
│   │       │   │   │   ├── bdist.py
│   │       │   │   │   ├── bdist_dumb.py
│   │       │   │   │   ├── bdist_rpm.py
│   │       │   │   │   ├── build.py
│   │       │   │   │   ├── build_clib.py
│   │       │   │   │   ├── build_ext.py
│   │       │   │   │   ├── build_py.py
│   │       │   │   │   ├── build_scripts.py
│   │       │   │   │   ├── check.py
│   │       │   │   │   ├── clean.py
│   │       │   │   │   ├── config.py
│   │       │   │   │   ├── install.py
│   │       │   │   │   ├── install_data.py
│   │       │   │   │   ├── install_egg_info.py
│   │       │   │   │   ├── install_headers.py
│   │       │   │   │   ├── install_lib.py
│   │       │   │   │   ├── install_scripts.py
│   │       │   │   │   ├── py37compat.py
│   │       │   │   │   ├── register.py
│   │       │   │   │   ├── sdist.py
│   │       │   │   │   └── upload.py
│   │       │   │   │
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _collections.py
│   │       │   │   ├── _functools.py
│   │       │   │   ├── _macos_compat.py
│   │       │   │   ├── _msvccompiler.py
│   │       │   │   ├── archive_util.py
│   │       │   │   ├── bcppcompiler.py
│   │       │   │   ├── ccompiler.py
│   │       │   │   ├── cmd.py
│   │       │   │   ├── config.py
│   │       │   │   ├── core.py
│   │       │   │   ├── cygwinccompiler.py
│   │       │   │   ├── debug.py
│   │       │   │   ├── dep_util.py
│   │       │   │   ├── dir_util.py
│   │       │   │   ├── dist.py
│   │       │   │   ├── errors.py
│   │       │   │   ├── extension.py
│   │       │   │   ├── fancy_getopt.py
│   │       │   │   ├── file_util.py
│   │       │   │   ├── filelist.py
│   │       │   │   ├── log.py
│   │       │   │   ├── msvc9compiler.py
│   │       │   │   ├── msvccompiler.py
│   │       │   │   ├── py38compat.py
│   │       │   │   ├── py39compat.py
│   │       │   │   ├── spawn.py
│   │       │   │   ├── sysconfig.py
│   │       │   │   ├── text_file.py
│   │       │   │   ├── unixccompiler.py
│   │       │   │   ├── util.py
│   │       │   │   ├── version.py
│   │       │   │   └── versionpredicate.py
│   │       │   │
│   │       │   ├── _vendor\
│   │       │   │   │
│   │       │   │   ├── __pycache__\
│   │       │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   ├── ordered_set.cpython-310.pyc
│   │       │   │   │   ├── typing_extensions.cpython-310.pyc
│   │       │   │   │   └── zipp.cpython-310.pyc
│   │       │   │   │
│   │       │   │   ├── importlib_metadata\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── _adapters.cpython-310.pyc
│   │       │   │   │   │   ├── _collections.cpython-310.pyc
│   │       │   │   │   │   ├── _compat.cpython-310.pyc
│   │       │   │   │   │   ├── _functools.cpython-310.pyc
│   │       │   │   │   │   ├── _itertools.cpython-310.pyc
│   │       │   │   │   │   ├── _meta.cpython-310.pyc
│   │       │   │   │   │   └── _text.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _adapters.py
│   │       │   │   │   ├── _collections.py
│   │       │   │   │   ├── _compat.py
│   │       │   │   │   ├── _functools.py
│   │       │   │   │   ├── _itertools.py
│   │       │   │   │   ├── _meta.py
│   │       │   │   │   └── _text.py
│   │       │   │   │
│   │       │   │   ├── importlib_resources\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── _adapters.cpython-310.pyc
│   │       │   │   │   │   ├── _common.cpython-310.pyc
│   │       │   │   │   │   ├── _compat.cpython-310.pyc
│   │       │   │   │   │   ├── _itertools.cpython-310.pyc
│   │       │   │   │   │   ├── _legacy.cpython-310.pyc
│   │       │   │   │   │   ├── abc.cpython-310.pyc
│   │       │   │   │   │   ├── readers.cpython-310.pyc
│   │       │   │   │   │   └── simple.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _adapters.py
│   │       │   │   │   ├── _common.py
│   │       │   │   │   ├── _compat.py
│   │       │   │   │   ├── _itertools.py
│   │       │   │   │   ├── _legacy.py
│   │       │   │   │   ├── abc.py
│   │       │   │   │   ├── readers.py
│   │       │   │   │   └── simple.py
│   │       │   │   │
│   │       │   │   ├── jaraco\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── context.cpython-310.pyc
│   │       │   │   │   │   └── functools.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── text\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   └── __init__.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   └── __init__.py
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── context.py
│   │       │   │   │   └── functools.py
│   │       │   │   │
│   │       │   │   ├── more_itertools\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── more.cpython-310.pyc
│   │       │   │   │   │   └── recipes.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── more.py
│   │       │   │   │   └── recipes.py
│   │       │   │   │
│   │       │   │   ├── packaging\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __about__.cpython-310.pyc
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── _manylinux.cpython-310.pyc
│   │       │   │   │   │   ├── _musllinux.cpython-310.pyc
│   │       │   │   │   │   ├── _structures.cpython-310.pyc
│   │       │   │   │   │   ├── markers.cpython-310.pyc
│   │       │   │   │   │   ├── requirements.cpython-310.pyc
│   │       │   │   │   │   ├── specifiers.cpython-310.pyc
│   │       │   │   │   │   ├── tags.cpython-310.pyc
│   │       │   │   │   │   ├── utils.cpython-310.pyc
│   │       │   │   │   │   └── version.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __about__.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _manylinux.py
│   │       │   │   │   ├── _musllinux.py
│   │       │   │   │   ├── _structures.py
│   │       │   │   │   ├── markers.py
│   │       │   │   │   ├── requirements.py
│   │       │   │   │   ├── specifiers.py
│   │       │   │   │   ├── tags.py
│   │       │   │   │   ├── utils.py
│   │       │   │   │   └── version.py
│   │       │   │   │
│   │       │   │   ├── pyparsing\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── actions.cpython-310.pyc
│   │       │   │   │   │   ├── common.cpython-310.pyc
│   │       │   │   │   │   ├── core.cpython-310.pyc
│   │       │   │   │   │   ├── exceptions.cpython-310.pyc
│   │       │   │   │   │   ├── helpers.cpython-310.pyc
│   │       │   │   │   │   ├── results.cpython-310.pyc
│   │       │   │   │   │   ├── testing.cpython-310.pyc
│   │       │   │   │   │   ├── unicode.cpython-310.pyc
│   │       │   │   │   │   └── util.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── diagram\
│   │       │   │   │   │   │
│   │       │   │   │   │   ├── __pycache__\
│   │       │   │   │   │   │   └── __init__.cpython-310.pyc
│   │       │   │   │   │   │
│   │       │   │   │   │   └── __init__.py
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── actions.py
│   │       │   │   │   ├── common.py
│   │       │   │   │   ├── core.py
│   │       │   │   │   ├── exceptions.py
│   │       │   │   │   ├── helpers.py
│   │       │   │   │   ├── results.py
│   │       │   │   │   ├── testing.py
│   │       │   │   │   ├── unicode.py
│   │       │   │   │   └── util.py
│   │       │   │   │
│   │       │   │   ├── tomli\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── _parser.cpython-310.pyc
│   │       │   │   │   │   ├── _re.cpython-310.pyc
│   │       │   │   │   │   └── _types.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _parser.py
│   │       │   │   │   ├── _re.py
│   │       │   │   │   └── _types.py
│   │       │   │   │
│   │       │   │   ├── __init__.py
│   │       │   │   ├── ordered_set.py
│   │       │   │   ├── typing_extensions.py
│   │       │   │   └── zipp.py
│   │       │   │
│   │       │   ├── command\
│   │       │   │   │
│   │       │   │   ├── __pycache__\
│   │       │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   ├── alias.cpython-310.pyc
│   │       │   │   │   ├── bdist_egg.cpython-310.pyc
│   │       │   │   │   ├── bdist_rpm.cpython-310.pyc
│   │       │   │   │   ├── build.cpython-310.pyc
│   │       │   │   │   ├── build_clib.cpython-310.pyc
│   │       │   │   │   ├── build_ext.cpython-310.pyc
│   │       │   │   │   ├── build_py.cpython-310.pyc
│   │       │   │   │   ├── develop.cpython-310.pyc
│   │       │   │   │   ├── dist_info.cpython-310.pyc
│   │       │   │   │   ├── easy_install.cpython-310.pyc
│   │       │   │   │   ├── editable_wheel.cpython-310.pyc
│   │       │   │   │   ├── egg_info.cpython-310.pyc
│   │       │   │   │   ├── install.cpython-310.pyc
│   │       │   │   │   ├── install_egg_info.cpython-310.pyc
│   │       │   │   │   ├── install_lib.cpython-310.pyc
│   │       │   │   │   ├── install_scripts.cpython-310.pyc
│   │       │   │   │   ├── py36compat.cpython-310.pyc
│   │       │   │   │   ├── register.cpython-310.pyc
│   │       │   │   │   ├── rotate.cpython-310.pyc
│   │       │   │   │   ├── saveopts.cpython-310.pyc
│   │       │   │   │   ├── sdist.cpython-310.pyc
│   │       │   │   │   ├── setopt.cpython-310.pyc
│   │       │   │   │   ├── test.cpython-310.pyc
│   │       │   │   │   ├── upload.cpython-310.pyc
│   │       │   │   │   └── upload_docs.cpython-310.pyc
│   │       │   │   │
│   │       │   │   ├── __init__.py
│   │       │   │   ├── alias.py
│   │       │   │   ├── bdist_egg.py
│   │       │   │   ├── bdist_rpm.py
│   │       │   │   ├── build.py
│   │       │   │   ├── build_clib.py
│   │       │   │   ├── build_ext.py
│   │       │   │   ├── build_py.py
│   │       │   │   ├── develop.py
│   │       │   │   ├── dist_info.py
│   │       │   │   ├── easy_install.py
│   │       │   │   ├── editable_wheel.py
│   │       │   │   ├── egg_info.py
│   │       │   │   ├── install.py
│   │       │   │   ├── install_egg_info.py
│   │       │   │   ├── install_lib.py
│   │       │   │   ├── install_scripts.py
│   │       │   │   ├── launcher manifest.xml
│   │       │   │   ├── py36compat.py
│   │       │   │   ├── register.py
│   │       │   │   ├── rotate.py
│   │       │   │   ├── saveopts.py
│   │       │   │   ├── sdist.py
│   │       │   │   ├── setopt.py
│   │       │   │   ├── test.py
│   │       │   │   ├── upload.py
│   │       │   │   └── upload_docs.py
│   │       │   │
│   │       │   ├── config\
│   │       │   │   │
│   │       │   │   ├── __pycache__\
│   │       │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   ├── _apply_pyprojecttoml.cpython-310.pyc
│   │       │   │   │   ├── expand.cpython-310.pyc
│   │       │   │   │   ├── pyprojecttoml.cpython-310.pyc
│   │       │   │   │   └── setupcfg.cpython-310.pyc
│   │       │   │   │
│   │       │   │   ├── _validate_pyproject\
│   │       │   │   │   │
│   │       │   │   │   ├── __pycache__\
│   │       │   │   │   │   ├── __init__.cpython-310.pyc
│   │       │   │   │   │   ├── error_reporting.cpython-310.pyc
│   │       │   │   │   │   ├── extra_validations.cpython-310.pyc
│   │       │   │   │   │   ├── fastjsonschema_exceptions.cpython-310.pyc
│   │       │   │   │   │   ├── fastjsonschema_validations.cpython-310.pyc
│   │       │   │   │   │   └── formats.cpython-310.pyc
│   │       │   │   │   │
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── error_reporting.py
│   │       │   │   │   ├── extra_validations.py
│   │       │   │   │   ├── fastjsonschema_exceptions.py
│   │       │   │   │   ├── fastjsonschema_validations.py
│   │       │   │   │   └── formats.py
│   │       │   │   │
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _apply_pyprojecttoml.py
│   │       │   │   ├── expand.py
│   │       │   │   ├── pyprojecttoml.py
│   │       │   │   └── setupcfg.py
│   │       │   │
│   │       │   ├── extern\
│   │       │   │   │
│   │       │   │   ├── __pycache__\
│   │       │   │   │   └── __init__.cpython-310.pyc
│   │       │   │   │
│   │       │   │   └── __init__.py
│   │       │   │
│   │       │   ├── __init__.py
│   │       │   ├── _deprecation_warning.py
│   │       │   ├── _entry_points.py
│   │       │   ├── _imp.py
│   │       │   ├── _importlib.py
│   │       │   ├── _itertools.py
│   │       │   ├── _path.py
│   │       │   ├── _reqs.py
│   │       │   ├── archive_util.py
│   │       │   ├── build_meta.py
│   │       │   ├── cli-32.exe
│   │       │   ├── cli-64.exe
│   │       │   ├── cli-arm64.exe
│   │       │   ├── cli.exe
│   │       │   ├── dep_util.py
│   │       │   ├── depends.py
│   │       │   ├── discovery.py
│   │       │   ├── dist.py
│   │       │   ├── errors.py
│   │       │   ├── extension.py
│   │       │   ├── glob.py
│   │       │   ├── gui-32.exe
│   │       │   ├── gui-64.exe
│   │       │   ├── gui-arm64.exe
│   │       │   ├── gui.exe
│   │       │   ├── installer.py
│   │       │   ├── launch.py
│   │       │   ├── logging.py
│   │       │   ├── monkey.py
│   │       │   ├── msvc.py
│   │       │   ├── namespaces.py
│   │       │   ├── package_index.py
│   │       │   ├── py34compat.py
│   │       │   ├── sandbox.py
│   │       │   ├── script (dev).tmpl
│   │       │   ├── script.tmpl
│   │       │   ├── unicode_utils.py
│   │       │   ├── version.py
│   │       │   ├── wheel.py
│   │       │   └── windows_support.py
│   │       │
│   │       ├── setuptools-65.5.0.dist-info\
│   │       │   ├── INSTALLER
│   │       │   ├── LICENSE
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   ├── REQUESTED
│   │       │   ├── WHEEL
│   │       │   ├── entry_points.txt
│   │       │   └── top_level.txt
│   │       │
│   │       └── distutils-precedence.pth
│   │
│   │
│   ├── Scripts\
│   │   ├── Activate.ps1
│   │   ├── activate
│   │   ├── activate.bat
│   │   ├── deactivate.bat
│   │   ├── pip.exe
│   │   ├── pip3.10.exe
│   │   ├── pip3.exe
│   │   ├── python.exe
│   │   ├── pythonw.exe
│   │   └── rptree.exe
│   │
│   └── pyvenv.cfg
│
├── Geek4Geek.py
├── Report.docx
├── floyd.py
├── floyd_rec.py
├── performance_test.py
├── performance_test_2.py
├── requirements.txt
└── testing.py
```
