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


    return factors.get(resolution,1)




# ==========================
# AI MODEL FACTOR
# ==========================

def get_ai_model_factor(model):


    factors = {


        "YOLOv8":1,


        "YOLOv10":1.3,


        "Detectron":1.5


    }


    return factors.get(model,1)




# ==========================
# MAIN CALCULATION
# ==========================

def calculate_requirements(customer_data):


    cameras = customer_data["camera_count"]


    fps = customer_data["fps"]


    resolution = customer_data["resolution"]


    ai_model = customer_data["ai_model"]


    latency = customer_data["latency"]



    # ==========================
    # FACTORS
    # ==========================


    resolution_factor = get_resolution_factor(

        resolution

    )


    model_factor = get_ai_model_factor(

        ai_model

    )



    processing_factor = 2



    optimization_factor = model_factor




    # ==========================
    # WORKLOAD SCORE
    # ==========================


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
    # VRAM
    # ==========================


    if ai_model == "YOLOv8":

        model_memory = 2


    elif ai_model == "YOLOv10":

        model_memory = 3


    else:

        model_memory = 4



    camera_memory = cameras * 0.2


    safety_margin = 1



    vram_required = (

        model_memory

        +

        camera_memory

        +

        safety_margin

    )




    # ==========================
    # CUDA
    # ==========================


    cuda_required = (

        workload_score

        *

        processing_factor

    )




    # ==========================
    # TENSOR
    # ==========================


    if ai_model == "YOLOv10":

        ai_model_complexity_factor = 100


    elif ai_model == "YOLOv8":

        ai_model_complexity_factor = 50


    else:

        ai_model_complexity_factor = 120



    tensor_required = ai_model_complexity_factor




    # ==========================
    # FP16
    # ==========================


    fp16_required = (

        fps

        *

        cameras

        *

        model_factor

        /

        100

    )




    # ==========================
    # INT8
    # ==========================


    int8_required = (

        workload_score

        *

        optimization_factor

    )




    # ==========================
    # LATENCY ADJUSTMENT
    # ==========================


    if latency == "Real-time":


        fp16_required = fp16_required * 1.5


        int8_required = int8_required * 1.5




    # ==========================
    # RETURN ALL VALUES
    # ==========================


    return {


        "workload_score": workload_score,


        "vram_required": round(vram_required,2),


        "cuda_required": round(cuda_required,0),


        "tensor_required": tensor_required,


        "fp16_required": round(fp16_required,2),


        "int8_required": round(int8_required,2),



        # intermediate values


        "resolution_factor": resolution_factor,


        "model_factor": model_factor,


        "processing_factor": processing_factor,


        "ai_model_complexity_factor": ai_model_complexity_factor,


        "optimization_factor": optimization_factor,



        # VRAM breakdown


        "model_memory": model_memory,


        "camera_memory": camera_memory,


        "safety_margin": safety_margin

    }
