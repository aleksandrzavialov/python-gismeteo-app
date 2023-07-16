def abs_path_from_project(relative_path: str):
    import
    from pathlib import Path

    return (
        Path(python_wikipedia_mobile.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )