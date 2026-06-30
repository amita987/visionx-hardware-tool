# ==========================
# CALCULATION ENGINE
# ==========================


# ==========================
# RESOLUTION FACTOR
# ==========================


def get_resolution_factor(resolution):


    factors = {


        "1080p": 1,

        "2K": 1.5,

        "4K": 2,

        "8K": 4

    }


    return factors.get(

        resolution,

        1

    )



# ==========================
# AI MODEL FACTOR
# ==========================


def get_ai_model_factor(model):


    factors = {


        "YOLOv8": 1,


        "YOLOv10": 1.3,


        "Detectron": 1.5


    }


    return factors.get(

        model,

        1

    )



# ==========================
# MAIN CALCULATION FUNCTION
# ==========================


def calculate_requirements(customer_data):


    cameras = customer_data["camera_count"]


    fps = customer_data["fps"]


    resolution = customer_data["resolution"]


    ai_model = customer_data["ai_model"]


    latency = customer_data["latency"]



    # ==========================
    # WORKLOAD SCORE
    # ==========================


    resolution_factor = get_resolution_factor(

        resolution

    )


    model_factor = get_ai_model_factor(

        ai_model

    )



    workload_score = (

        cameras

        *

        fps

        *

        resolution_factor

        *

        model_factor

    )



    # ==========================
    # VRAM REQUIRED
    # ==========================


    # Model memory

    if ai_model == "YOLOv8":

        model_memory = 2


    elif ai_model == "YOLOv10":

        model_memory = 3


    else:

        model_memory = 4



    # Camera buffer

    camera_memory = cameras * 0.2



    # Safety margin

    safety_margin = 1



    vram_required = (

        model_memory

        +

        camera_memory

        +

        safety_margin

    )



    # ==========================
    # CUDA REQUIREMENT
    # ==========================


    cuda_required = workload_score * 2



    # ==========================
    # TENSOR REQUIREMENT
    # ==========================


    if ai_model == "YOLOv10":

        tensor_required = 100


    elif ai_model == "YOLOv8":

        tensor_required = 50


    else:

        tensor_required = 120



    # ==========================
    # FP16 REQUIREMENT
    # ==========================


    fp16_required = (

        cameras

        *

        fps

        *

        model_factor

        /

        10

    )



    # ==========================
    # INT8 REQUIREMENT
    # ==========================


    int8_required = (

        workload_score

        *

        model_factor

    )



    # ==========================
    # LATENCY ADJUSTMENT
    # ==========================


    if latency == "Real-time":


        fp16_required = fp16_required * 1.5


        int8_required = int8_required * 1.5




    return {


        "workload_score": workload_score,


        "vram_required": round(vram_required,2),


        "cuda_required": round(cuda_required,0),


        "tensor_required": tensor_required,


        "fp16_required": round(fp16_required,2),


        "int8_required": round(int8_required,2)


    }
