import io
from dearprudence import read_params, write_params, Cmip6Record, SimpleRun


def test_read_params_reads():
    """
    Test that dodola.read_params reads two params from JSON string in parameter file
    """
    expected_p1 = SimpleRun(
        target="historical",
        variable_id="tasmax",
        historical=Cmip6Record(
            activity_id="CMIP",
            experiment_id="historical",
            table_id="day",
            variable_id="tasmax",
            source_id="ACCESS-CM2",
            institution_id="CSIRO-ARCCSS",
            member_id="r1i1p1f1",
            grid_label="gn",
            version="20191108",
        ),
        ssp=Cmip6Record(
            activity_id="ScenarioMIP",
            experiment_id="ssp370",
            table_id="day",
            variable_id="tasmax",
            source_id="ACCESS-CM2",
            institution_id="CSIRO-ARCCSS",
            member_id="r1i1p1f1",
            grid_label="gn",
            version="20191108",
        ),
    )
    expected_p2 = SimpleRun(
        target="ssp",
        variable_id="tasmax",
        historical=Cmip6Record(
            activity_id="CMIP",
            experiment_id="historical",
            table_id="day",
            variable_id="tasmax",
            source_id="ACCESS-CM2",
            institution_id="CSIRO-ARCCSS",
            member_id="r1i1p1f1",
            grid_label="gn",
            version="20191108",
        ),
        ssp=Cmip6Record(
            activity_id="ScenarioMIP",
            experiment_id="ssp370",
            table_id="day",
            variable_id="tasmax",
            source_id="ACCESS-CM2",
            institution_id="CSIRO-ARCCSS",
            member_id="r1i1p1f1",
            grid_label="gn",
            version="20191108",
        ),
    )
    fl = io.StringIO(
        """jobs: |
  [
    {
      "target": "historical",
      "variable_id": "tasmax",
      "historical": {
        "activity_id": "CMIP",
        "experiment_id": "historical",
        "table_id": "day",
        "variable_id": "tasmax",
        "source_id": "ACCESS-CM2",
        "institution_id": "CSIRO-ARCCSS",
        "member_id": "r1i1p1f1",
        "grid_label": "gn",
        "version": "20191108"
      },
      "ssp": {
        "activity_id": "ScenarioMIP",
        "experiment_id": "ssp370",
        "table_id": "day",
        "variable_id": "tasmax",
        "source_id": "ACCESS-CM2",
        "institution_id": "CSIRO-ARCCSS",
        "member_id": "r1i1p1f1",
        "grid_label": "gn",
        "version": "20191108"
      }
    },
    {
      "target": "ssp",
      "variable_id": "tasmax",
      "historical": {
        "activity_id": "CMIP",
        "experiment_id": "historical",
        "table_id": "day",
        "variable_id": "tasmax",
        "source_id": "ACCESS-CM2",
        "institution_id": "CSIRO-ARCCSS",
        "member_id": "r1i1p1f1",
        "grid_label": "gn",
        "version": "20191108"
      },
      "ssp": {
        "activity_id": "ScenarioMIP",
        "experiment_id": "ssp370",
        "table_id": "day",
        "variable_id": "tasmax",
        "source_id": "ACCESS-CM2",
        "institution_id": "CSIRO-ARCCSS",
        "member_id": "r1i1p1f1",
        "grid_label": "gn",
        "version": "20191108"
      }
    }
  ]
"""
    )
    p1, p2 = read_params(fl)
    assert p1 == expected_p1
    assert p2 == expected_p2


def test_write_params_writes(tmp_path):
    """
    Test that dodola.write_params writes two SimpleRuns to a parameter file.
    """
    params = [
        SimpleRun(
            target="historical",
            variable_id="tasmax",
            historical=Cmip6Record(
                activity_id="CMIP",
                experiment_id="historical",
                table_id="day",
                variable_id="tasmax",
                source_id="ACCESS-CM2",
                institution_id="CSIRO-ARCCSS",
                member_id="r1i1p1f1",
                grid_label="gn",
                version="20191108",
            ),
            ssp=Cmip6Record(
                activity_id="ScenarioMIP",
                experiment_id="ssp370",
                table_id="day",
                variable_id="tasmax",
                source_id="ACCESS-CM2",
                institution_id="CSIRO-ARCCSS",
                member_id="r1i1p1f1",
                grid_label="gn",
                version="20191108",
            ),
        ),
        SimpleRun(
            target="ssp",
            variable_id="tasmax",
            historical=Cmip6Record(
                activity_id="CMIP",
                experiment_id="historical",
                table_id="day",
                variable_id="tasmax",
                source_id="ACCESS-CM2",
                institution_id="CSIRO-ARCCSS",
                member_id="r1i1p1f1",
                grid_label="gn",
                version="20191108",
            ),
            ssp=Cmip6Record(
                activity_id="ScenarioMIP",
                experiment_id="ssp370",
                table_id="day",
                variable_id="tasmax",
                source_id="ACCESS-CM2",
                institution_id="CSIRO-ARCCSS",
                member_id="r1i1p1f1",
                grid_label="gn",
                version="20191108",
            ),
        ),
    ]
    path = tmp_path / "test_write_params_writes.yaml"
    expected_contents = """jobs: |
  [
    {
      "target": "historical",
      "variable_id": "tasmax",
      "historical": {
        "activity_id": "CMIP",
        "experiment_id": "historical",
        "table_id": "day",
        "variable_id": "tasmax",
        "source_id": "ACCESS-CM2",
        "institution_id": "CSIRO-ARCCSS",
        "member_id": "r1i1p1f1",
        "grid_label": "gn",
        "version": "20191108"
      },
      "ssp": {
        "activity_id": "ScenarioMIP",
        "experiment_id": "ssp370",
        "table_id": "day",
        "variable_id": "tasmax",
        "source_id": "ACCESS-CM2",
        "institution_id": "CSIRO-ARCCSS",
        "member_id": "r1i1p1f1",
        "grid_label": "gn",
        "version": "20191108"
      }
    },
    {
      "target": "ssp",
      "variable_id": "tasmax",
      "historical": {
        "activity_id": "CMIP",
        "experiment_id": "historical",
        "table_id": "day",
        "variable_id": "tasmax",
        "source_id": "ACCESS-CM2",
        "institution_id": "CSIRO-ARCCSS",
        "member_id": "r1i1p1f1",
        "grid_label": "gn",
        "version": "20191108"
      },
      "ssp": {
        "activity_id": "ScenarioMIP",
        "experiment_id": "ssp370",
        "table_id": "day",
        "variable_id": "tasmax",
        "source_id": "ACCESS-CM2",
        "institution_id": "CSIRO-ARCCSS",
        "member_id": "r1i1p1f1",
        "grid_label": "gn",
        "version": "20191108"
      }
    }
  ]
"""
    write_params(path, params)
    contents = path.read_text()
    assert contents == expected_contents


def test_reread_written_params(tmp_path):
    """
    Test dodola.read_params reads matching params written by dodola.write_params.
    """
    params_written = [
        SimpleRun(
            target="ssp",
            variable_id="tasmax",
            historical=Cmip6Record(
                activity_id="CMIP",
                experiment_id="historical",
                table_id="day",
                variable_id="tasmax",
                source_id="ACCESS-CM2",
                institution_id="CSIRO-ARCCSS",
                member_id="r1i1p1f1",
                grid_label="gn",
                version="20191108",
            ),
            ssp=Cmip6Record(
                activity_id="ScenarioMIP",
                experiment_id="ssp370",
                table_id="day",
                variable_id="tasmax",
                source_id="ACCESS-CM2",
                institution_id="CSIRO-ARCCSS",
                member_id="r1i1p1f1",
                grid_label="gn",
                version="20191108",
            ),
        )
    ]
    path = tmp_path / "test_reread_written_params.yaml"

    write_params(path, params_written)
    params_reread = read_params(str(path))
    assert params_written == params_reread
