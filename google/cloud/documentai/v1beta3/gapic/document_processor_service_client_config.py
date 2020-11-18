config = {
    "interfaces": {
        "google.cloud.documentai.v1beta3.DocumentProcessorService": {
            "retry_codes": {
                "retry_policy_1_codes": ["DEADLINE_EXCEEDED", "UNAVAILABLE"],
                "no_retry_codes": [],
            },
            "retry_params": {
                "retry_policy_1_params": {
                    "initial_retry_delay_millis": 100,
                    "retry_delay_multiplier": 1.3,
                    "max_retry_delay_millis": 60000,
                    "initial_rpc_timeout_millis": 120000,
                    "rpc_timeout_multiplier": 1.0,
                    "max_rpc_timeout_millis": 120000,
                    "total_timeout_millis": 120000,
                },
                "no_retry_params": {
                    "initial_retry_delay_millis": 0,
                    "retry_delay_multiplier": 0.0,
                    "max_retry_delay_millis": 0,
                    "initial_rpc_timeout_millis": 0,
                    "rpc_timeout_multiplier": 1.0,
                    "max_rpc_timeout_millis": 0,
                    "total_timeout_millis": 0,
                },
            },
            "methods": {
                "ProcessDocument": {
                    "timeout_millis": 120000,
                    "retry_codes_name": "retry_policy_1_codes",
                    "retry_params_name": "retry_policy_1_params",
                },
                "BatchProcessDocuments": {
                    "timeout_millis": 120000,
                    "retry_codes_name": "retry_policy_1_codes",
                    "retry_params_name": "retry_policy_1_params",
                },
                "ReviewDocument": {
                    "timeout_millis": 120000,
                    "retry_codes_name": "retry_policy_1_codes",
                    "retry_params_name": "retry_policy_1_params",
                },
            },
        }
    }
}