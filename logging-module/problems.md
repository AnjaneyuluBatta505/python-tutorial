# logging module

1. **Basic Logging Setup** – Create a simple script that logs messages at different severity levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).  
2. **Rotating Log Files** – Implement rotating logs using `RotatingFileHandler` to limit log file size and create backups.  
3. **Time-based Log Rotation** – Use `TimedRotatingFileHandler` to rotate logs daily, hourly, or at custom intervals.  
4. **Logging to Multiple Destinations** – Configure logging to write messages to both the console and a file simultaneously.  
5. **Custom Log Formatting** – Modify log message format to include timestamps, log levels, and module names.  
6. **Logging Exceptions** – Automatically log exceptions with stack traces using `logging.exception()` inside a try-except block.  
7. **JSON Log Formatter** – Create a custom log formatter that outputs log messages in JSON format.  
8. **Log Filtering** – Implement a custom log filter to log only messages from a specific module or function.  
9. **Logging in a Multi-Threaded Application** – Set up logging for a multi-threaded program, ensuring thread-safe log writes.  
10. **Centralized Logging System** – Send logs to a remote server or a centralized logging service (e.g., ELK stack, Graylog).  
