def test_get_activities_returns_expected_payload_and_no_store_header(client):
    # Arrange

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert response.headers.get("cache-control") == "no-store"

    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data

    chess_club = data["Chess Club"]
    assert "description" in chess_club
    assert "schedule" in chess_club
    assert "max_participants" in chess_club
    assert "participants" in chess_club
    assert isinstance(chess_club["participants"], list)