package ai.giskard.web.rest.project;

import ai.giskard.IntegrationTest;
import ai.giskard.repository.ProjectRepository;
import ai.giskard.security.AuthoritiesConstants;
import ai.giskard.service.InitService;
import ai.giskard.service.dto.ml.ProjectPostDTO;
import ai.giskard.web.rest.controllers.ProjectController;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.hamcrest.CoreMatchers;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.http.MediaType;
import org.springframework.security.test.context.support.WithMockUser;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.transaction.annotation.Transactional;

import static org.assertj.core.api.Assertions.assertThat;
import static org.hamcrest.CoreMatchers.containsString;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

/**
 * Integration tests for the {@link ProjectController} REST controller with AITester authorities
 */
@AutoConfigureMockMvc
@IntegrationTest
@WithMockUser(username = "aitest", authorities = AuthoritiesConstants.AITESTER)
class AITesterProjectResourceIT extends AICreatorProjectResourceIT {

    @Autowired
    private ProjectRepository projectRepository;

    @Autowired
    private MockMvc restUserMockMvc;

    @Autowired
    private InitService initService;

    @Override
    public void initKeys() {
        this.USERKEY = initService.getUserName("aitest");
        this.PROJECTKEY = initService.getProjectName("aitest");
        this.OTHERUSERKEY = initService.getUserName("admin");
        this.OTHERPROJECTKEY = initService.getProjectName("admin");
    }

    /**
     * Get all Projects
     *
     * @throws Exception
     */
    @Override
    @Test
    @Transactional
    void getAllProjects() throws Exception {
        restUserMockMvc.perform(get("/api/v2/project").accept(MediaType.APPLICATION_JSON))
            .andExpect(status().isOk())
            .andExpect(content().contentType(MediaType.APPLICATION_JSON_VALUE))
            .andExpect(content().string(containsString(PROJECTKEY)))
            .andExpect(content().string(CoreMatchers.not(containsString(initService.getProjectName("aicreator")))))
            .andExpect(content().string(CoreMatchers.not(containsString(OTHERPROJECTKEY))));
    }

    /**
     * Create new Project
     * should return Unauthorized
     *
     * @throws Exception
     */
    @Override
    @Test
    @Transactional
    void create() throws Exception {
        ProjectPostDTO projectDTO = new ProjectPostDTO();
        projectDTO.setName("createdProject");
        projectDTO.setKey("keyProject");
        restUserMockMvc.perform(post("/api/v2/project").contentType(MediaType.APPLICATION_JSON)
            .content(new ObjectMapper().writeValueAsString(projectDTO)))
            .andExpect(status().is4xxClientError());
        assertThat(projectRepository.findOneByName("createdProject")).isEmpty();
    }

}
