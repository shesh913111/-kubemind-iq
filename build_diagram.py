from graphviz import Digraph

dot = Digraph("KubeMindIQ", format="png")

dot.attr(rankdir="TB")

dot.node("User", "User")
dot.node("KubeMind", "KubeMind IQ")
dot.node("Foundry", "Microsoft Foundry IQ")

dot.node("Runbooks", "AKS Runbooks")
dot.node("Docs", "Kubernetes Docs")
dot.node("History", "Incident History")

dot.node("Reasoning", "Multi-Step Reasoning Agent")
dot.node("RCA", "Root Cause Analysis")
dot.node("Reco", "Recommendations")

dot.edge("User", "KubeMind")
dot.edge("KubeMind", "Foundry")

dot.edge("Foundry", "Runbooks")
dot.edge("Foundry", "Docs")
dot.edge("Foundry", "History")

dot.edge("Runbooks", "Reasoning")
dot.edge("Docs", "Reasoning")
dot.edge("History", "Reasoning")

dot.edge("Reasoning", "RCA")
dot.edge("RCA", "Reco")

dot.render("diagrams/architecture", cleanup=True)

print("Architecture diagram created successfully!")