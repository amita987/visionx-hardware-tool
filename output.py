# ==========================
# OUTPUT ENGINE
# ==========================

from calculation_engine import calculate_requirements


# ==========================
# FINAL OUTPUT FUNCTION
# ==========================

def generate_output(customer_input):


    # Step 1: Get calculated values

    results = calculate_requirements(customer_input)


    # Step 2: Format final output for Streamlit UI

    output = {
        # ======================
        # INTERMEDIATE VARIABLES
        # ======================


        "Resolution Factor": results["resolution_factor"],


        "AI Model Factor": results["model_factor"],


        "Model Memory (GB)": results["model_memory"],


        "Camera Memory (GB)": results["camera_memory"],


        "Safety Margin (GB)": results["safety_margin"],

        # ======================
        # CORE METRICS
        # ======================

        "Workload Score": results["workload_score"],

        "VRAM Required (GB)": results["vram_required"],

        "CUDA Required": results["cuda_required"],

        "Tensor Required": results["tensor_required"],

        "FP16 Required": results["fp16_required"],

        "INT8 Required": results["int8_required"],


        # ======================
        # SUMMARY (UI FRIENDLY)
        # ======================

        "Summary": {


            "System Type": "AI Vision System",


            "Performance Level":

                "High"

                if results["workload_score"] > 1000

                else "Medium"


        }


    }


    return output
