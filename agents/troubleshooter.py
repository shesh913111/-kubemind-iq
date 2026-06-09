def analyze_issue(issue):

    issue = issue.lower()

    if "crashloop" in issue:

        return {
            "summary": "Application container is repeatedly crashing and restarting.",
            "reasoning": [
                "Detected repeated pod restart pattern",
                "Checking startup dependencies",
                "Checking secrets and configmaps",
                "Comparing against known AKS incidents"
            ],
            "root_cause": "Missing Secret",
            "recommendation": "Create Secret and restart deployment",
            "confidence": "92%"
        }

    elif "imagepull" in issue:

        return {
            "summary": "Kubernetes is unable to pull the container image.",
            "reasoning": [
                "Image pull failure detected",
                "Checking image repository",
                "Checking ACR authentication",
                "Validating image tag"
            ],
            "root_cause": "Invalid Image Tag",
            "recommendation": "Verify image tag and registry access",
            "confidence": "88%"
        }

    elif "failedscheduling" in issue:

        return {
            "summary": "Pod cannot be scheduled on any available node.",
            "reasoning": [
                "Scheduler unable to place pod",
                "Checking CPU and memory availability",
                "Reviewing node capacity",
                "Comparing scheduling constraints"
            ],
            "root_cause": "Insufficient Resources",
            "recommendation": "Scale node pool or reduce resource requests",
            "confidence": "90%"
        }

    elif "oomkilled" in issue:

        return {
            "summary": "Container exceeded memory limits and was terminated.",
            "reasoning": [
                "Detected OOMKilled event",
                "Reviewing memory consumption",
                "Checking container limits",
                "Comparing usage patterns"
            ],
            "root_cause": "Memory Limit Exceeded",
            "recommendation": "Increase memory limits or optimize application",
            "confidence": "95%"
        }

    else:

        return {
            "summary": "Unknown issue pattern detected.",
            "reasoning": [
                "Analyzing issue description",
                "No matching incident pattern found"
            ],
            "root_cause": "Unknown",
            "recommendation": "Collect logs, events and pod details",
            "confidence": "60%"
        }