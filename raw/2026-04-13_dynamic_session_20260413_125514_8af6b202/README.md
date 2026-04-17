# Object Escape Analysis Report

**Target:** `tests\java\target\escape-tests-1.0-SNAPSHOT.jar;tests\java\target\classes:com.escape.tests.cases.Case294SerializationRoundtripSafe08:execute`
**Language:** java
**Analyzer Version:** 1.0.0
**Session ID:** 010670d0-c7bb-4b9b-99ce-9179a8a47ea5
**Generated:** 2026-04-13 12:55:14

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
| `<bridge-startup>` | ❌ CRASH | ✓ NO | No escaping references detected | Runtime Crash: Exception in thread "main" java.lang.NoClassDefFoundError: com/google/gson/GsonBuilder | Inspect stack trace and target function side effects; rerun in dynamic mode with verbose logging. |

