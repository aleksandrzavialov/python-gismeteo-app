def abs_path_from_project(relative_path: str):
    import python_gismeteo_mobile
    from pathlib import Path

    return (
        Path(python_gismeteo_mobile.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
