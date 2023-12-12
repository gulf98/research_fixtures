def test_check_dgdat_connection(dgdat_db):
    print("checking connection")
    assert dgdat_db == "dgdat"
