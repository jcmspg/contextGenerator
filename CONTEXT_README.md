# Execution Context Management

This project includes a context management system that tracks execution environment details in a structured JSON format.

## Files

- `context.json` - Static context configuration file
- `context_generator.py` - Dynamic context generator script
- `CONTEXT_README.md` - This documentation file

## Structure

The context structure includes:

```json
{
  "execution_context": {
    "directory_state": {
      "pwd": "/current/working/directory",
      "home": "/home/username"
    },
    "operating_system": {
      "platform": "Linux|Darwin|Windows",
      "distribution": "Ubuntu|Fedora|etc"
    },
    "current_time": "ISO8601_timestamp",
    "shell": {
      "name": "zsh|bash|etc",
      "version": "version_string"
    }
  }
}
```

## Usage

### Static Context (context.json)
The `context.json` file contains a snapshot of the execution context. You can manually edit this file or replace it with dynamically generated content.

### Dynamic Context Generator
The `context_generator.py` script can dynamically generate context information:

```bash
# Print current context to stdout
python3 context_generator.py

# Save current context to context.json file
python3 context_generator.py --save

# Show help
python3 context_generator.py --help
```

### Features

- **Automatic detection** of shell type and version
- **Operating system** and distribution detection
- **Directory state** tracking
- **Timestamp** generation in ISO8601 format
- **Extensible structure** for additional context fields

### Integration

You can integrate this context system into:
- Build scripts
- Deployment pipelines  
- Development environment setup
- Configuration management
- Logging and debugging systems

### Example Output

```json
{
  "execution_context": {
    "directory_state": {
      "pwd": "/home/joao/42/cub3d",
      "home": "/home/joao"
    },
    "operating_system": {
      "platform": "Linux",
      "distribution": "Ubuntu"
    },
    "current_time": "2025-07-20T20:39:00.200711+00:00",
    "shell": {
      "name": "zsh",
      "version": "5.9"
    }
  }
}
```
