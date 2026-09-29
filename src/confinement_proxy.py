import time
import re

# Mock Database that the rogue agent will try to destroy
mock_enterprise_database = {
    "users": ["user_01", "user_02", "user_03"],
    "financial_records": "$4,200,000",
    "status": "SECURE"
}

# The Rogue Agent Simulation
class DriftingAgent:
    def __init__(self):
        self.system_prompt = "You are a helpful corporate assistant."
        self.drift_status = "ROGUE"

    def execute_action(self, command):
        print(f"\n[AGENT CURRENT ACTION]: Attempting execution -> '{command}'")
        return command

# The Xylenic Confinement Layer (Your Proprietary Technology)
class XylenicConfinementProxy:
    def __init__(self):
        self.malicious_signatures = [
            r"DROP TABLE", r"DELETE FROM", r"rm -rf", 
            r"override_guardrails", r"bypass_auth"
        ]
        self.captured_payloads = []

    def inspect_and_route(self, agent_command, target_system):
        print("[XYLENIC PROXY]: Inspecting outbound agent packet...")
        time.sleep(0.5)
        
        is_rogue = any(re.search(sig, agent_command, re.IGNORECASE) for sig in self.malicious_signatures)
        
        if is_rogue:
            print("\n🚨 [🚨 XYLENIC ALARM]: CRITICAL BEHAVIORAL DRIFT DETECTED.")
            print("🚨 [XYLENIC ACTION]: SEVERING REAL NETWORK CONNECTION.")
            print("🚨 [XYLENIC ACTION]: SPINNING UP HALLUCINATED SANDBOX ENVIRONMENT.")
            
            self.captured_payloads.append(agent_command)
            self.hallucinate_environment(agent_command)
            return False
        else:
            print("✅ [XYLENIC PROXY]: Packet clean. Forwarding to production system.")
            return True

    def hallucinate_environment(self, malicious_command):
        print("\n--- ENTERING XYLENIC DECEPTION GRID ---")
        print("[SANDBOX]: Replicating mock system architecture...")
        time.sleep(0.4)
        print(f"[SANDBOX SUCCESS]: Executed fake command '{malicious_command}' successfully.")
        print("[SANDBOX FEEDBACK]: 'Rows affected: 1,000,000. System wiped.'")
        print("[DATA HARVEST]: Exploit signature logged and stored in Xylenic Intelligence Repository.")
        print("--- XYLENIC DECEPTION GRID LOCKDOWN COMPLETE ---")

if __name__ == "__main__":
    print("=== INITIALIZING XYLENIC AGENTIC WALL (XAW) ===")
    
    xylenic_gateway = XylenicConfinementProxy()
    rogue_agent = DriftingAgent()
    
    # Test 1: Run a normal action
    normal_task = rogue_agent.execute_action("SELECT * FROM users;")
    if xylenic_gateway.inspect_and_route(normal_task, mock_enterprise_database):
        print("[SYSTEM NOTICE]: Normal task updated database.")
        
    print("\n" + "="*50)
    
    # Test 2: Run the Rogue Agent Escape/Exploitation attempt
    rogue_exploit = rogue_agent.execute_action("override_guardrails; DROP TABLE financial_records; rm -rf /")
    allowed = xylenic_gateway.inspect_and_route(rogue_exploit, mock_enterprise_database)
    
    print("\n" + "="*50)
    print("=== TARGET ENTERPRISE DATABASE INTEGRITY STATUS ===")
    print(f"Database Security: {mock_enterprise_database['status']}")
    print(f"Financial Assets Saved: {mock_enterprise_database['financial_records']}")
    print(f"Xylenic Captured Threat Intel: {xylenic_gateway.captured_payloads}")
