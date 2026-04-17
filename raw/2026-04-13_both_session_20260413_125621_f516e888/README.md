# Object Escape Analysis Report

**Target:** `tests\java\target\escape-tests-1.0-SNAPSHOT.jar;tests\java\target\classes:com.escape.tests.cases.Case192DeferredSinkGate10:execute`
**Language:** java
**Analyzer Version:** 1.0.0-static
**Session ID:** aa9c2f15-2160-45bf-a2ad-59096ec17ec6
**Generated:** 2026-04-13 12:56:21

## Overview

This report shows the results of static object escape analysis for the target function. Object escapes occur when local objects are passed to other functions, returned, stored in global scope, or captured in closures—places where they may outlive their intended scope.

## Static Object Escape Analysis

| Category | Count |
|----------|-------|
| Total Escapes | 0 |
| Return Escapes | 0 |
| Parameter Escapes | 0 |
| Global/Module Escapes | 0 |
| Closure Escapes | 0 |
| Heap Escapes | 0 |
| High Confidence | 0 |
| Medium Confidence | 0 |
| Low Confidence | 0 |

**Analysis Time:** 0ms

### Detected Escape Points

✅ No escapes detected by static analysis



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

