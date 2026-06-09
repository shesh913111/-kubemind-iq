# CrashLoopBackOff

Cause:
Application startup failure

Checks:
kubectl logs <pod>
kubectl describe pod <pod>

Fix:
Verify Secrets
Verify ConfigMaps

# ImagePullBackOff

Cause:
Image not found

Fix:
Verify image tag
Check ACR permissions

# FailedScheduling

Cause:
Insufficient CPU or Memory

Fix:
Scale node pool
Reduce resource requests