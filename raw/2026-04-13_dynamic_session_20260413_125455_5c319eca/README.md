# Object Escape Analysis Report

**Target:** `tests\java\target\escape-tests-1.0-SNAPSHOT.jar;tests\java\target\classes:com.escape.tests.cases.Case091ReconcileProfile:execute`
**Language:** java
**Analyzer Version:** 1.0.0
**Session ID:** 8f698531-793d-4a1c-a5b9-a6f85eea880e
**Generated:** 2026-04-13 12:54:55

## Overview

This report shows the results of static object escape analysis for the target function. Object escapes occur when local objects are passed to other functions, returned, stored in global scope, or captured in closures—places where they may outlive their intended scope.



## Execution Verification

| Metric | Value |
|--------|-------|
| Executions | 1 |
| Successes | 0 ✓ |
| Crashes | 1 ✗ |
| Crash Rate | 100.0% |

## Vulnerabilities

✅ **No vulnerabilities detected**

## Error Diagnostics

### Error Categories

| Category | Count |
|----------|-------|
| Runtime Crash | 1 |

### Representative Errors

- **Runtime Crash** for input `<bridge-startup>`: Runtime Crash: Exception in thread "main" java.lang.NoClassDefFoundError: com/google/gson/GsonBuilder  
  Suggested action: Inspect stack trace and target function side effects; rerun in dynamic mode with verbose logging.


## Execution Results

| Input | Status | Escape | Details | Error | Suggested Action |
|-------|--------|--------|----------|-------|------------------|
| `<bridge-startup>` | ❌ CRASH | 🚨 YES | No escaping references detected | Runtime Crash: Exception in thread "main" java.lang.NoClassDefFoundError: com/google/gson/GsonBuilder | Inspect stack trace and target function side effects; rerun in dynamic mode with verbose logging. |

