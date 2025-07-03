from agent import graph

def test_agent():
    test_input = {
        "today": {"revenue": 1000, "cost": 800, "customers": 40},
        "yesterday": {"revenue": 900, "cost": 600, "customers": 40}
    }

    result = graph.invoke(test_input)

    assert isinstance(result, dict)
    assert "status" in result
    assert "alerts" in result
    assert "recommendations" in result
    assert result["status"] in ["Profit", "Loss"]

    print("✅ Test passed!")

if __name__ == "__main__":
    test_agent()