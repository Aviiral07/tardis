import pytest
from tardis.io.configuration.config_reader import Configuration

def test_invalid_config_key_raises_error(tmp_path):
    bad_config = tmp_path / "bad.yml"
    bad_config.write_text(
        """
        supernova:
          luminosity_requested: 1e9
        plasma:
          wrong_key: true
        """
    )

    with pytest.raises(Exception):
        Configuration.from_yaml(bad_config)
